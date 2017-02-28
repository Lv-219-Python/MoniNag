"""This module holds basic daemon class which will be inherited by specific child daemons"""

import atexit
import os
import signal
import sys
import time


class Daemon(object):
    """Linux Daemon boilerplate.

    Must be inherited and can't be run. Otherwise raise NotImplementedError.

    Attributes:
        daemon_name(str): daemon name in processes.
            Also pid file will be created with name <daemon_name>.pid

        pid_file_path(str): path to directory where pid file
            will be created and stored while daemon is running.
            If path doesn't exist it will be created.

        logger(Logger): specified logging.Logger object to write logs.
    """

    def __init__(self, daemon_name, pid_file_path, logger):

        self.daemon_name = daemon_name
        self.pid_file = '{0}/{1}.pid'.format(pid_file_path, daemon_name)
        self.logger = logger

        # Set process name
        try:
            import setproctitle
            setproctitle.setproctitle(self.daemon_name)
        except Exception as err:
            self.logger.error('Can not set daemon name. Error: {0}'.format(err))

    def delete_pid(self):
        """Delete the pid file."""

        os.remove(self.pid_file)

    def daemonize(self):
        """Create daemon."""

        # Fork 1 to spin off the child that will spawn the deamon.
        if os.fork():
            sys.exit()

        # This is the child.
        # cd to root for a guarenteed working dir.
        os.chdir('/')

        # Clear the session id to clear the controlling TTY.
        os.setsid()
        # Set the umask so we have access to all files created by the daemon.
        os.umask(0)

        # fork 2 ensures we can't get a controlling TTY.
        if os.fork():
            sys.exit()

        # This is a child that can't ever have a controlling TTY.
        # Shut down stdin, stderr, stdout
        with open('/dev/null', 'r') as dev_null:
            os.dup2(dev_null.fileno(), sys.stdin.fileno())
            os.dup2(dev_null.fileno(), sys.stderr.fileno())
            os.dup2(dev_null.fileno(), sys.stdout.fileno())

        # Write pid file
        # Before file creation, make sure we'll delete the pid file on exit!
        atexit.register(self.delete_pid)

        pid = str(os.getpid())
        self.logger.debug('Daemon created with pid {0}.'.format(pid))

        with open(self.pid_file, 'w+') as pid_file:
            pid_file.write('{0}'.format(pid))

    def get_pid_by_file(self):
        """Return the pid read from the pid file."""

        try:
            with open(self.pid_file, 'r') as pid_file:
                pid = int(pid_file.read().strip())
            return pid
        except IOError:
            return

    def start(self):
        """Start the daemon."""

        if self.get_pid_by_file():
            print('PID file {0} exists.\nIs the deamon already running?'.format(self.pid_file))
            sys.exit(1)

        print('Starting {0} ...'.format(self.daemon_name))
        self.daemonize()
        self.run()

    def status(self):
        """Get daemon Status """

        if self.get_pid_by_file():
            pidfile = open(self.pid_file, 'r')
            print('Daemon is currently running. PID: {}'.format(pidfile.read()))
        else:
            print('Daemon is not running.')

    def stop(self):
        """Stop the daemon."""

        pid = self.get_pid_by_file()
        if not pid:
            print("PID file {0} doesn't exist.\nIs the daemon not running?".format(self.pid_file))
            return

        print('Stopping {0} ...'.format(self.daemon_name))

        # Kill daemon.
        try:
            while True:
                os.kill(pid, signal.SIGTERM)
                time.sleep(0.1)
        except OSError as err:
            if 'No such process' in err.strerror and os.path.exists(self.pid_file):
                os.remove(self.pid_file)
            else:
                sys.exit(1)

    def restart(self):
        """Restart the deamon."""
        self.stop()
        self.start()

    def run(self):
        """The main loop of the daemon. Must be specified by  child class."""
        raise NotImplementedError
