import os
import sys
import time

import django

from daemon import Daemon

# Path to project directory where manage.py is located
project_path = '../'
sys.path.append(project_path)

# This is so Django knows where to find stuff
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moninag.settings')
django.setup()

from check.models import Check


class CollectorDaemon(Daemon):
    """Collector daemon

    Daemon should start in a foreground.
    Daemon should fetch all checks from DB on start and refresh every 5 minutes.
    Daemon should write logs to moninag_collector.log file.

    Attributes:
        daemon_name(str): daemon name in processes.
            Also pid file will be created with name <daemon_name>.pid

        pid_file_path(str): path to directory where pid file
            will be created and stored while daemon is running.
            If path doesn't exist it will be created.

        logger(Logger): specified logging.Logger object to write logs.

        frequency(int): frequency time in seconds to repeat the task.
    """

    def __init__(self, daemon_name, pid_file_path, logger, frequency):
        """If pid_file_path directory doesn't exist create it"""
        if not os.path.exists(pid_file_path):
            os.makedirs(pid_file_path)
        super(CollectorDaemon, self).__init__(daemon_name, pid_file_path, logger)
        self.frequency = frequency

    def run(self):
        """ The main loop of the daemon. """

        while True:
            self.perform_task()
            time.sleep(self.frequency)

    def perform_task(self):
        """Get all checks and write to log file"""
        self.logger.info('{} started'.format(self.daemon_name))
        try:
            self.logger.info('Fetching Data')
            checks = Check.objects.all().order_by('id')
            for check in checks:
                self.logger.debug('Check #{id}: (Name: {name}) (Service #:{service_id}) '
                                  '(Plugin Name: {pluginname}) (Target Port: {targ_port}) '
                                  '(Run Frequency: {run_freq}sec) '.format(id=check.id,
                                                                           name=check.name,
                                                                           service_id=check.service.id,
                                                                           pluginname=check.plugin_name,
                                                                           targ_port=check.target_port,
                                                                           run_freq=check.run_freq))

            self.logger.info('Fetching Finished. Number of '
                             'records: {amount}'.format(amount=Check.objects.all().count()))
        except Exception as error:
            self.logger.error(str(error))
