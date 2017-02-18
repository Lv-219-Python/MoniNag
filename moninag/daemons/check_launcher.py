import datetime
import django
import os
import sys
import time
from multiprocessing import Process, Queue, current_process
import subprocess
import django.db

# Path to project directory where manage.py is located
PROJECT_PATH = '../'
sys.path.append(PROJECT_PATH)

# This is so Django knows where to find stuff
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moninag.settings')
django.setup()

from check.models import Check


def perform_check(check_id, command, freq):
    while True:
        print('starting process {}', check_id)
        output = subprocess.Popen(command,
                                  stdout=subprocess.PIPE,
                                  shell=True).communicate()

        # print(datetime.datetime.now(), command, output)
        output = output[0].split()

        if b'OK' in output[1]:
            # print('\t OK')
            this_check = Check.objects.get(id=check_id)
            this_check.service.status = 'OK'
            this_check.service.save()

        elif b'WARNING' in output[1]:
            # print('\t Warning')
            this_check = Check.objects.get(id=check_id)
            this_check.service.status = 'Warning'
            this_check.service.save()
        else:
            # print('\t Fail')
            this_check = Check.objects.get(id=check_id)
            this_check.service.status = 'Fail'
            this_check.service.save()

        print('ending process {}', check_id)
        time.sleep(freq)


def check_collector(storage):
    checks = Check.objects.all()

    storage_keys = set(storage.keys())
    check_keys = set(checks.in_bulk().keys())

    check_dict = {}
    for check in checks:
        check_dict[check.id] = {}
        check_dict[check.id]['command'] = check.plugin.template.format(host=check.service.server.address)
        check_dict[check.id]['freq'] = check.run_freq

    # print(check_keys)
    # print(storage_keys)
    # added items
    if check_keys - storage_keys:
        for key in check_keys - storage_keys:
            # print('added item')
            storage[key] = check_dict[key]
            storage[key]['command'] = check_dict[key]['command']
            storage[key]['freq'] = check_dict[key]['freq']

    # deleted items
    if storage_keys - check_keys:
        for key in storage_keys - check_keys:
            # print('deleted item')
            del storage[key]

    # update items
    for check_id in check_dict:
        if check_dict[check_id]['command'] != storage[check_id]['command']:
            # print('upd')
            storage[check_id]['command'] = check_dict[check_id]['command']
        if check_dict[check_id]['freq'] != storage[check_id]['freq']:
            storage[check_id]['freq'] = check_dict[check_id]['freq']


def main():
    storage = {}
    processes = []
    django.db.connections.close_all()
    q = Queue()

    while True:
        print('starting main')
        new_storage = storage.copy()
        check_collector(new_storage)
        # print('>>>>>>>>>>>>>', storage)
        # print('>>>>>>>>>>>>>', new_storage)
        for check_id in new_storage:
            if 'pid' not in new_storage[check_id]:
                p = Process(target=perform_check, args=(check_id,
                                                        new_storage[check_id]['command'],
                                                        new_storage[check_id]['freq'],))

                p.name = 'Process{}'.format(check_id)
                p.start()

                processes.append(p)
                # print('starting process {} with pid: {}'.format(storage[check]['command'], p.pid))
                new_storage[check_id]['pid'] = p.pid

        storage = new_storage.copy()
        # for p in processes:
        #     p.join()
        print('ending main')
        time.sleep(30)


if __name__ == '__main__':
    main()
