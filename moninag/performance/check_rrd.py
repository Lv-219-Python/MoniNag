"""This file contains wrapper functions of RRD to use with checks"""

import logging
import os
import re
from pathlib import Path

import rrdtool

# Current file path
CURRENT_FILE_PATH = Path(__file__)

# Path to folder, where all RRDs will be stored
RRD_PATH = str(CURRENT_FILE_PATH.parents[0]) + '/rrd/'

# Path to folder, where all checks graphs will be stored
GRAPH_PATH = str(CURRENT_FILE_PATH.parents[1]) + '/static/img/perfgraphs/'

# Path to folder, where log files will be stored
LOG_PATH = str(CURRENT_FILE_PATH.parents[0]) + '/log'

# RRD size (30 days in seconds)
RRD_SIZE = 2592000

# Extra time added to heartbeat
HEARTBEAT_EXTRA_TIME = 60

# List of graphs to be created
GRAPHS = [
    {
        'graph_dir': GRAPH_PATH + 'hour/',
        'time_period': 60 * 60,
    },
    {
        'graph_dir': GRAPH_PATH + 'day/',
        'time_period': 60 * 60 * 24,
    },
    {
        'graph_dir': GRAPH_PATH + 'week/',
        'time_period': 60 * 60 * 24 * 7,
    },
    {
        'graph_dir': GRAPH_PATH + 'month/',
        'time_period': 60 * 60 * 24 * 30,
    },
]

# Time parser for check outputs
TIME_PARSER = re.compile(r'(?:time|rta)=(\d+?\.\d+|\d+)(s|ms)')

# Create logger
try:
    os.makedirs(LOG_PATH)
except OSError:
    # Path already exist
    pass

LOGGER = logging.getLogger('check_rrd')
HANDLER = logging.FileHandler('{0}/check_rrd.log'.format(LOG_PATH))
FORMATTER = logging.Formatter('%(asctime)s - %(levelname)7s - %(message)s',
                              '%Y-%m-%d %H:%M:%S')
HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(HANDLER)
LOGGER.setLevel(logging.INFO)


def create(check_id, heartbeat):
    """Create check RRD"""

    rrd_name = _generate_name(RRD_PATH, check_id, 'rrd')

    if exist(rrd_name):
        LOGGER.error('CREATE RRD: check#{0}, FAIL: RRD already exist.'.format(check_id))
        return None

    try:
        os.makedirs(RRD_PATH)
    except OSError:
        # Path already exist
        pass

    heartbeat += HEARTBEAT_EXTRA_TIME

    try:
        rrdtool.create(rrd_name,
                       '--step', '1',
                       'DS:time:GAUGE:{0}:U:U'.format(heartbeat),
                       'RRA:AVERAGE:0.5:1:{0}'.format(RRD_SIZE))

        LOGGER.info('CREATE RRD: check#{0}, heartbeat = {1}: {2}.'.format(check_id,
                                                                          heartbeat,
                                                                          rrd_name))

    except rrdtool.OperationalError as error:
        LOGGER.error('CREATE RRD: check#{0}, FAIL: {1}.'.format(check_id, str(error)))


def exist(file_name):
    """Check if file exist"""

    return os.path.isfile(file_name)


def get_info(check_id):
    """Get RRD information for check"""

    rrd_name = _generate_name(RRD_PATH, check_id, 'rrd')

    if exist(rrd_name):
        return rrdtool.info(rrd_name)


def generate_perfgraphs(check_id):
    """Generate check graphs from GRAPHS list"""

    for graph in GRAPHS:
        generate_graph(check_id, **graph)


def generate_graph(check_id, graph_dir, time_period=3600, width=800, height=300):
    """Generate check graph"""

    rrd_name = _generate_name(RRD_PATH, check_id, 'rrd')

    if not exist(rrd_name):
        LOGGER.error('GRAPH RRD: check#{0}, FAIL: RRD does not exist.'.format(check_id))
        return None

    try:
        os.makedirs(graph_dir)
    except OSError:
        # Path already exist
        pass

    graph_name = _generate_name(graph_dir, check_id, 'png')

    end_time = get_info(check_id)['last_update']

    try:
        # Check if graph file is up-to-date
        file_time = os.path.getmtime(graph_name)
        if file_time >= end_time:
            return None

    except OSError:
        # File does not exist
        pass

    start_time = end_time - time_period

    try:
        rrdtool.graph(graph_name,
                      '--title', 'Check output time',
                      '--start', str(start_time),
                      '--end', str(end_time),
                      '--width', str(width),
                      '--height', str(height),
                      '--alt-y-grid',
                      '--border', '1',
                      '--color', 'BACK#333333',
                      '--color', 'GRID#5095CE',
                      '--color', 'MGRID#5095CE',
                      '--color', 'AXIS#888888',
                      '--color', 'ARROW#888888',
                      '--color', 'FRAME#000',
                      '--color', 'FONT#E0E0E0',
                      '--color', 'CANVAS#1E1E1E',
                      '--color', 'SHADEA#888888',
                      '--color', 'SHADEB#888888',
                      '--font', 'TITLE:13:.',
                      '--font', 'LEGEND:10:.',
                      '--font', 'AXIS:9:.',
                      '--font', 'WATERMARK:8:.',
                      '--font', 'UNIT:10:.',
                      '--grid-dash', '1:1',
                      '--lower-limit', '0',
                      '--slope-mode',
                      '--vertical-label', 'ms',
                      '--watermark', 'MoniNag',
                      'TEXTALIGN:left',
                      'DEF:times={0}:time:AVERAGE'.format(rrd_name),
                      'AREA:times#5095CE:average time (ms)')

        LOGGER.info('GRAPH RRD: check#{0}: {1}.'.format(check_id, graph_name))

    except rrdtool.OperationalError as error:
        LOGGER.error('GRAPH RRD: check#{0}, FAIL: {1}.'.format(check_id, str(error)))


def remove(check_id):
    """Remove check RRD and graph"""

    rrd_name = _generate_name(RRD_PATH, check_id, 'rrd')
    if exist(rrd_name):
        os.remove(rrd_name)
        LOGGER.info('REMOVE RRD: check#{0}: {1}.'.format(check_id, rrd_name))

    for graph in GRAPHS:
        graph_name = _generate_name(graph['graph_dir'], check_id, 'png')
        if exist(graph_name):
            os.remove(graph_name)
            LOGGER.info('REMOVE GRAPH: check#{0}: {1}.'.format(check_id, graph_name))


def set_heartbeat(check_id, heartbeat):
    """Set check RRD heartbeat"""

    rrd_name = _generate_name(RRD_PATH, check_id, 'rrd')

    if not exist(rrd_name):
        LOGGER.error('TUNE RRD: check#{0}, FAIL: rrd does not exist.'.format(check_id))
        return None

    heartbeat += HEARTBEAT_EXTRA_TIME

    try:
        rrdtool.tune(rrd_name,
                     '--heartbeat', 'time:{0}'.format(heartbeat))

        LOGGER.info('TUNE RRD: check#{0}, heartbeat = {1}.'.format(check_id, heartbeat))

    except rrdtool.OperationalError as error:
        LOGGER.error('TUNE RRD: check#{0}, FAIL: {1}.'.format(check_id, str(error)))


def update(check_id, check_output):
    """Update check RRD"""

    rrd_name = _generate_name(RRD_PATH, check_id, 'rrd')
    if not exist(rrd_name):
        LOGGER.error('UPDATE RRD: check#{0}, FAIL: rrd does not exist.'.format(check_id))
        return None

    value = _parse_time(check_output)
    if value is None:
        LOGGER.error('UPDATE RRD: check#{0}, FAIL: value is None.'.format(check_id))
        return None

    new_data = 'N:{0}'.format(value)

    try:
        rrdtool.update(rrd_name, new_data)
        LOGGER.info('UPDATE RRD: check#{0}, value = {1}.'.format(check_id, value))

    except rrdtool.OperationalError as error:
        LOGGER.error('UPDATE RRD: check#{0}, FAIL: {1}.'.format(check_id, str(error)))


def _generate_name(path, check_id, extension):
    """Generate RRD name for check"""

    return '{0}check_{1}.{2}'.format(path, check_id, extension)


def _parse_time(output):
    """Parse time from output text"""

    parsed_data = TIME_PARSER.findall(output)
    if not parsed_data:
        return None

    output_time = float(parsed_data[0][0])
    measurement = parsed_data[0][1]

    if measurement == 's':
        output_time *= 1000

    return output_time
