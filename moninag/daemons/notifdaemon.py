import os
import sys
import time

import django

from daemon import Daemon


# Path to project directory where manage.py is located
PROJECT_PATH = '../'
sys.path.append(PROJECT_PATH)

# This is so Django knows where to find stuff
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moninag.settings')
django.setup()


from service.models import Service


class NotificationDaemon(Daemon):
    """Notification daemon.

    Fetches services with not-OK status from database
    with given frequency as well as related server and user.
    Daemon write logs to log file.

    Attributes:
        daemon_name(str): daemon name in processes.
            Also pid file will be created with name <daemon_name>.pid

        pid_file_path(str): path to directory where pid file
            will be created and stored while daemon is running.
            If path doesn't exist it will be created.

        logger(Logger): specified logging.Logger object to write logs.

        frequency(int): frequency time in seconds to repeat the task.

        statuses(list): list of statuses which should be fetched by daemon.
    """

    def __init__(self, daemon_name, pid_file_path, logger, frequency, statuses):

        # If pid_file_path directory doesn't exist create it
        if not os.path.exists(pid_file_path):
            os.makedirs(pid_file_path)
        super(NotificationDaemon, self).__init__(daemon_name, pid_file_path, logger)

        self.frequency = frequency
        self.statuses = statuses

    def run(self):
        """The main loop of the daemon."""

        while True:
            self.perform_task()
            time.sleep(self.frequency)

    def perform_task(self):
        """Get services with fail status and write to log file."""

        self.logger.debug('Start fetching services with {} statuses...'.format(self.statuses))

        try:
            services = Service.get_by_statuses(self.statuses)

            self.logger.debug('...{} services with {} statuses.'.format(len(services),
                                                                        self.statuses))

            for service in services:
                self.logger.info(
                    'Service #{id}: {name}, '
                    'status: {status}, '
                    'server #{server_id}: {server_name}, '
                    'user #{user_id}: {user_email}'.format(id=service.id,
                                                           name=service.name,
                                                           status=service.status,
                                                           server_id=service.server.id,
                                                           server_name=service.server.name,
                                                           user_id=service.server.user.id,
                                                           user_email=service.server.user.email))

            self.logger.debug('..fetching finished.'.format(self.statuses))

        except Exception as error:
            self.logger.error(str(error))
