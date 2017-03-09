import os
import random
import sys
from pathlib import Path

import django
import rrdtool

# Path to project directory where manage.py is located
PROJECT_PATH = str(Path(__file__).parents[1])
sys.path.append(PROJECT_PATH)

# This is so Django knows where to find stuff
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moninag.settings')
django.setup()

from check.models import Check
from performance import check_rrd


end_time = 1489497600
start_time = end_time - check_rrd.RRD_SIZE


checks = Check.objects.all()

for check in checks:
    print('Generate for check#{0}: {1} ...'.format(check.id, check.name))

    rrd_name = check_rrd._generate_name(check_rrd.RRD_PATH, check.id, 'rrd')
    check_rrd.remove(check.id)

    rrdtool.create(rrd_name,
                   '--start', str(start_time - 10),
                   '--step', '1',
                   'DS:time:GAUGE:{0}:U:U'.format(check.run_freq + 60),
                   'RRA:AVERAGE:0.5:1:{0}'.format(check_rrd.RRD_SIZE))

    for time in range(start_time, end_time, check.run_freq):
        value = random.randint(1, 1000)
        new_data = '{0}:{1}'.format(time, value)

        rrdtool.update(rrd_name, new_data)

    check_rrd.generate_perfgraphs(check.id)
