import logging
import os
import sys

from collectordaemon import CollectorDaemon

# Absolute path to this script
current_path = os.path.abspath(os.curdir)

# Set daemon process name
daemon_name = 'moninag_collector_daemon'

# Frequency in seconds
frequency = 300

# Set path to directory with pid files
pid_file_path = current_path + '/tmp'

# Set path to directory with log files
log_file_path = current_path + '/log'

# If log_file_path directory doesn't exist create it
if not os.path.exists(log_file_path):
    os.makedirs(log_file_path)

# Create logger
logger = logging.getLogger('moninag_collector')

# Logger format
formatter = logging.Formatter('%(asctime)2s - %(levelname)2s - %(message)s')

# Log file handler
handler = logging.FileHandler('{0}/{1}.log'.format(log_file_path, daemon_name))

# Set logger output level
logger.setLevel(logging.DEBUG)

handler.setFormatter(formatter)
logger.addHandler(handler)

# Starting daemon with command line
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {0} start | stop | restart'.format(sys.argv[0]))
        sys.exit(2)

    daemon = CollectorDaemon(daemon_name, pid_file_path, logger, frequency)

    if 'start' == sys.argv[1]:
        daemon.start()
    elif 'stop' == sys.argv[1]:
        daemon.stop()
    elif 'restart' == sys.argv[1]:
        daemon.restart()
    else:
        print("Unknown command '{0}'".format(sys.argv[1]))
        sys.exit(2)
