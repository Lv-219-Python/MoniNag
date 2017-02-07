import argparse
import logging
import os

from collectordaemon import CollectorDaemon

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
logger = logging.getLogger('moninag_collector')

# Logger format
formatter = logging.Formatter('%(asctime)s\t%(levelname)s\t%(name)s: %(message)s')

# Log file handler
handler = logging.FileHandler('{0}/{1}.log'.format(LOG_FILE_PATH, DAEMON_NAME))

handler.setFormatter(formatter)
logger.addHandler(handler)

# Starting daemon with command line
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Collector daemon runner.')

    parser.add_argument('command', choices={'start', 'status', 'stop', 'restart'},
                        help='command applied to collector daemon')

    level_group = parser.add_mutually_exclusive_group()

    level_group.add_argument('-d', '--debug', action='store_true',
                             help='set debug output level')

    level_group.add_argument('-i', '--info', action='store_true',
                             help='set info output level')

    level_group.add_argument('-w', '--warning', action='store_true',
                             help='set warning output level')

    level_group.add_argument('-e', '--error', action='store_true',
                             help='set error output level')

    args = parser.parse_args()

    # Set default logger output level
    level = logging.INFO
    str_level = 'INFO'

    if args.debug:
        level = logging.DEBUG
        str_level = 'DEBUG'
    elif args.warning:
        level = logging.WARNING
        str_level = 'WARNING'
    elif args.error:
        level = logging.ERROR
        str_level = 'ERROR'

    logger.setLevel(level)
    daemon = CollectorDaemon(DAEMON_NAME, PID_FILE_PATH, logger, FREQUENCY)
    if 'start' == args.command:
        print('Output level set to {}'.format(str_level))
        daemon.start()
    elif 'status' == args.command:
        daemon.status()
    elif 'stop' == args.command:
        daemon.stop()
    elif 'restart' == args.command:
        print('Output level set to {}'.format(str_level))
        daemon.restart()
