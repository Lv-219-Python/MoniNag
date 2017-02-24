"""
This module provides methods for launching check commands as multiple processes and
synchronizing them to database.
"""
import functools
import copy
import os
import subprocess
import sys
import time
from multiprocessing import Process

import django
import django.db
from django.utils import timezone

# Path to project directory where manage.py is located
PROJECT_PATH = '../'
sys.path.append(PROJECT_PATH)

# This is so Django knows where to find stuff
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moninag.settings')
django.setup()

from check.models import Check


def retry_query(tries=3, delay=1):
    """Decorator function handling reconnection issues to DB."""

    def retry_wrapper(func):
        """Wrapper function.
            :params func: function to call
            :return: wrapper function
            """

        @functools.wraps(func)
        def inner(*args, **kwargs):
            """Inner wrapper function
            :params *args: list of different arguments
                    *kwargs: dictionary of different arguments
            """

            mtries = tries
            mdelay = delay

            while mtries:
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    if mtries:
                        time.sleep(mdelay)
                mtries -= 1

        return inner

    return retry_wrapper


@retry_query()
def status_change(check_id, output):
    """
    Method which changes check and service status according to output of the command.
    :param check_id: id of the check for which the
    :param output: command output from terminal
    """

    output_list = output[0].split()
    this_check = Check.objects.get(id=check_id)

    if b'OK' in output_list[1]:
        # Set check status to OK
        this_check.status = 'OK'

    elif b'WARNING' in output_list[1]:
        # Set check status to WARNING
        this_check.status = 'WARNING'
    else:
        # Set check status to Fail
        this_check.status = 'FAIL'

    # Set check output/last_run data
    this_check.output = output[0].decode('utf-8')
    this_check.last_run = timezone.now()
    this_check.save()
    this_check.update_service_status()
    time.sleep(1)


def perform_check(check_id, command, freq):
    """
    Method which performs check in an infinite loop. Each check has its own subprocess
    :param check_id: check_id
    :param command: check command to be laubuntu zoom screenunched
    :param freq: check run frequency
    """

    while True:
        # Execute a child program in a new process.
        output = subprocess.Popen(command,
                                  stdout=subprocess.PIPE,
                                  shell=True).communicate()

        status_change(check_id, output)

        time.sleep(freq)


def check_sync(storage):
    """
    This method performs database records collecting into storage and perform synchronization
    :param storage: storage in the memory which containts currently active checks
    """

    checks = Check.objects.all()

    storage_keys = set(storage.keys())
    check_keys = set(checks.in_bulk().keys())

    # Create a dict of checks which has check_id, command and run_frequency
    check_dict = {}
    for check in checks:
        check_dict[check.id] = {}

        # if this check needs port to run the command attach target_port to the command
        if '{port}' in check.plugin.template:
            command = check.plugin.template.format(host=check.service.server.address,
                                                   port=check.target_port)

            check_dict[check.id]['command'] = command

        else:
            command = check.plugin.template.format(host=check.service.server.address)
            check_dict[check.id]['command'] = command

        check_dict[check.id]['freq'] = check.run_freq

    # synchronize added items
    if check_keys - storage_keys:
        for key in check_keys - storage_keys:
            storage[key] = check_dict[key]
            storage[key]['command'] = check_dict[key]['command']
            storage[key]['freq'] = check_dict[key]['freq']

    # synchronize deleted items
    if storage_keys - check_keys:
        for key in storage_keys - check_keys:
            del storage[key]

    # synchronize update items
    for check_id in check_dict:
        if check_dict[check_id]['command'] != storage[check_id]['command']:
            storage[check_id]['command'] = check_dict[check_id]['command']

        if check_dict[check_id]['freq'] != storage[check_id]['freq']:
            storage[check_id]['freq'] = check_dict[check_id]['freq']


def start_process(check_id, storage, processes):
    """
    This method spawns a process which performs check
    :param check_id: id of the check in database
    :param storage: storage which contains checks to be launched
    :param processes: storage which contains processes which are currently running
    """

    process = Process(target=perform_check, args=(check_id,
                                                  storage[check_id]['command'],
                                                  storage[check_id]['freq'],))

    # Set process name to "Process+check_id"
    process.name = 'Process{}'.format(check_id)
    process.start()

    # Add process to processes dict with key=pid and value=processname
    processes[process.pid] = process
    storage[check_id]['pid'] = process.pid


def stop_process(check_id, storage, processes):
    """
    This method terminates processes for a deleted check
    :param check_id: deleted check_id
    :param storage: storage which contains checks to be launched
    :param processes: storage which contains processes which are currently running
    """

    processes[storage[check_id]['pid']].terminate()
    os.wait()
    del processes[storage[check_id]['pid']]


def check_launcher():
    """Main function which launches everything"""

    # Storage in memory which holds info about currently running checks
    storage = {}

    # Storage in memory which holds process info: process id and project objects
    processes = {}

    # Close previously opened connections (if the exist)
    django.db.connections.close_all()

    while True:
        # Making Copy in order to compare updates in data base
        new_storage = copy.deepcopy(storage)

        # Fetch data from database
        check_sync(new_storage)

        # Get storage keys in order to compare storages for changes
        old_keys = set(storage.keys())
        new_keys = set(new_storage.keys())

        # Get keys of elements in init storage and updated storage
        added_checks = new_keys.difference(old_keys)
        deleted_checks = old_keys.difference(new_keys)
        common_checks = new_keys.intersection(old_keys)

        # Launch new processes
        for check_id in added_checks:
            # Spawn new process with name Process#id, where id = check_id
            start_process(check_id, new_storage, processes)

        # Stop (kill) deleted check's prorcesses
        for check_id in deleted_checks:
            stop_process(check_id, storage, processes)

        for check_id in common_checks:
            if storage[check_id] != new_storage[check_id]:
                stop_process(check_id, storage, processes)
                # Spawn new process with name Process#id, where id = check_id
                start_process(check_id, new_storage, processes)

        storage = copy.deepcopy(new_storage)
        time.sleep(30)


if __name__ == '__main__':
    check_launcher()
