"""This module contains collector daemon starting script"""

import argparse
import logging
import os

from collectordaemon import CollectorDaemon  # pylint: disable=import-error

# Absolute path to this script
CURRENT_PATH = os.path.abspath(os.curdir)

# Set daemon process name
DAEMON_NAME = 'moninag_collector_daemon'

# Frequency in seconds
FREQUENCY = 300

# Set path to directory with pid files
PID_FILE_PATH = CURRENT_PATH + '/tmp'

# Set path to directory with log files
LOG_FILE_PATH = CURRENT_PATH + '/log'

# If log_file_path directory doesn't exist create it
if not os.path.exists(LOG_FILE_PATH):
    os.makedirs(LOG_FILE_PATH)

# Create logger
LOGGER = logging.getLogger('moninag_collector')

# Logger format
FORMATTER = logging.Formatter('%(asctime)s\t%(levelname)s\t%(name)s: %(message)s')

# Log file handler
HANDLER = logging.FileHandler('{0}/{1}.log'.format(LOG_FILE_PATH, DAEMON_NAME))

HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(HANDLER)

# pylint: disable=duplicate-code
# Starting daemon with command line
if __name__ == '__main__':


    PARSER = argparse.ArgumentParser(description='Collector daemon runner.')

    PARSER.add_argument('command', choices={'start', 'status', 'stop', 'restart'},
                        help='command applied to collector daemon')

    LEVEL_GROUP = PARSER.add_mutually_exclusive_group()

    LEVEL_GROUP.add_argument('-d', '--debug', action='store_true',
                             help='set debug output level')

    LEVEL_GROUP.add_argument('-i', '--info', action='store_true',
                             help='set info output level')

    LEVEL_GROUP.add_argument('-w', '--warning', action='store_true',
                             help='set warning output level')

    LEVEL_GROUP.add_argument('-e', '--error', action='store_true',
                             help='set error output level')

    ARGS = PARSER.parse_args()

    # Set default logger output level
    LEVEL = logging.INFO
    STR_LEVEL = 'INFO'

    if ARGS.debug:
        LEVEL = logging.DEBUG
        STR_LEVEL = 'DEBUG'
    elif ARGS.warning:
        LEVEL = logging.WARNING
        STR_LEVEL = 'WARNING'
    elif ARGS.error:
        LEVEL = logging.ERROR
        STR_LEVEL = 'ERROR'

    LOGGER.setLevel(LEVEL)
    DAEMON = CollectorDaemon(DAEMON_NAME, PID_FILE_PATH, LOGGER, FREQUENCY)
    if ARGS.command == 'start':
        print('Output level set to {}'.format(STR_LEVEL))
        DAEMON.start()
    elif ARGS.command == 'status':
        DAEMON.status()
    elif ARGS.command == 'stop':
        DAEMON.stop()
    elif ARGS.command == 'restart':
        print('Output level set to {}'.format(STR_LEVEL))
        DAEMON.restart()
