"""This module provides methods for launching check commands as multiple processes and synchronizing them to database"""

import copy
import django
import django.db
import os
import subprocess
import sys
import time
from django.utils import timezone
from multiprocessing import Process

# Path to project directory where manage.py is located
PROJECT_PATH = '../'
sys.path.append(PROJECT_PATH)

# This is so Django knows where to find stuff
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moninag.settings')
django.setup()

from check.models import Check


def perform_check(check_id, command, freq):
    """
    Method which performs check in an infinite loop
    :param check_id: check_id
    :param command: check command to be launched
    :param freq: check run frequency
    """

    while True:

        # Execute a child program in a new process.
        output = subprocess.Popen(command,
                                  stdout=subprocess.PIPE,
                                  shell=True).communicate()

        output_list = output[0].split()

        # Check whether the check exists in database
        if Check.get_by_id(check_id):

            if b'OK' in output_list[1]:
                # Set check status to OK
                this_check = Check.objects.get(id=check_id)
                this_check.status = 'OK'
                this_check.output = output[0].decode('utf-8')
                this_check.last_run = timezone.now()
                this_check.save()

            elif b'WARNING' in output_list[1]:
                # Set check status to WARNING
                this_check = Check.objects.get(id=check_id)
                this_check.status = 'Warning'
                this_check.output = output[0].decode('utf-8')
                this_check.last_run = timezone.now()
                this_check.save()

            else:
                # Set check status to Fail
                this_check = Check.objects.get(id=check_id)
                this_check.status = 'Fail'
                this_check.output = output[0].decode('utf-8')
                this_check.last_run = timezone.now()
                this_check.save()

        # Perform freqeuency
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
            check_dict[check.id]['command'] = check.plugin.template.format(host=check.service.server.address,
                                                                           port=check.target_port)
        else:
            check_dict[check.id]['command'] = check.plugin.template.format(host=check.service.server.address)

        check_dict[check.id]['freq'] = check.run_freq

    # synchronize added items
    if check_keys - storage_keys:
        for key in check_keys - storage_keys:
            print('added item')
            storage[key] = check_dict[key]
            storage[key]['command'] = check_dict[key]['command']
            storage[key]['freq'] = check_dict[key]['freq']

    # synchronize deleted items
    if storage_keys - check_keys:
        for key in storage_keys - check_keys:
            print('deleted item')
            del storage[key]

    # synchronize update items
    for check_id in check_dict:
        if check_dict[check_id]['command'] != storage[check_id]['command']:
            print('upd')
            storage[check_id]['command'] = check_dict[check_id]['command']
        if check_dict[check_id]['freq'] != storage[check_id]['freq']:
            storage[check_id]['freq'] = check_dict[check_id]['freq']


def check_launcher():
    storage = {}
    processes = {}
    django.db.connections.close_all()

    while True:
        print('starting main')

        # Making Copy in order to compare updates in data base
        new_storage = copy.deepcopy(storage)

        # Fetch data from database
        check_sync(new_storage)

        # Get storage keys in order to compare storages for changes
        old_keys = set(storage.keys())
        new_keys = set(new_storage.keys())

        # Get keys of added_checks/deleted_checks/common_checks elements in init storage and updated storage
        added_checks = new_keys.difference(old_keys)
        deleted_checks = old_keys.difference(new_keys)
        common_checks = new_keys.intersection(old_keys)

        # Launch new processes
        for check_id in added_checks:
            # Spawn new process with name Process#id, where id = check_id
            p = Process(target=perform_check, args=(check_id,
                                                    new_storage[check_id]['command'],
                                                    new_storage[check_id]['freq'],))

            p.name = 'Process{}'.format(check_id)
            p.start()

            # Add process to processes dict with key=pid and value=processname
            processes[p.pid] = p
            new_storage[check_id]['pid'] = p.pid
            print('starting process with PID:', new_storage[check_id]['pid'])

        # Stop (kill) deleted check's prorcesses
        for check_id in deleted_checks:
            print('killing process with PID:', processes[storage[check_id]['pid']])
            processes[storage[check_id]['pid']].terminate()
            os.wait()
            del processes[storage[check_id]['pid']]

        for check_id in common_checks:
            if storage[check_id] != new_storage[check_id]:
                print('updating process', new_storage[check_id])
                print('killing process with PID:', new_storage[check_id]['pid'])
                processes[new_storage[check_id]['pid']].terminate()
                os.wait()
                del processes[new_storage[check_id]['pid']]
                # Spawn new process with name Process#id, where id = check_id
                p = Process(target=perform_check, args=(check_id,
                                                        new_storage[check_id]['command'],
                                                        new_storage[check_id]['freq'],))

                p.name = 'Process{}'.format(check_id)
                p.start()

                # Add process to processes dict with key=pid and value=processname
                processes[p.pid] = p
                new_storage[check_id]['pid'] = p.pid
                print('starting process with PID:', new_storage[check_id]['pid'])


        storage = copy.deepcopy(new_storage)
        time.sleep(30)


if __name__ == '__main__':
    check_launcher()
