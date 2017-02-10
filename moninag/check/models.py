from django.db import models

from service.models import Service


class Check(models.Model):
    """Check model class

    :attribute id: int - Autogenerated primary key.
    :attribute name: str - Check name
    :attribute plugin name: str - Plugin name.
    :attribute target_port: int - Define target port.
    :attribute run_freq: int - Define run frequency of plugin.
    :attribute service: int - ForeignKey to service id value.
    """

    name = models.CharField(max_length=20, default=0)
    plugin_name = models.CharField(max_length=20, default=0)
    target_port = models.IntegerField(default=0)
    run_freq = models.IntegerField(default=0)
    service = models.ForeignKey(Service)

    @staticmethod
    def create(name, plugin_name, target_port, run_freq, service):
        """Create and add check to database.

        :param name: str - Check name.
        :param plugin_name: str - Plugin name.
        :param target_port: int - Target port.
        :param run_freq: int - Run frequency.
        :param service: int - Service id.

        :return: Created check for success.
        """

        check = Check()

        check.name = name
        check.plugin_name = plugin_name
        check.target_port = target_port
        check.run_freq = run_freq
        check.service = service

        check.save()

        return check

    def update(self, name=None, plugin_name=None, target_port=None, run_freq=None):
        """Update check data.

        :param name: str - Check name.
        :param plugin_name: str - Plugin name.
        :param target_port: int - Target port.
        :param run_freq: int - Run frequency.

        :return: Updated check for success.
        """

        if name:
            self.name = name
        if plugin_name:
            self.plugin_name = plugin_name
        if target_port:
            self.target_port = target_port
        if run_freq:
            self.run_freq = run_freq

        self.save()

    @staticmethod
    def get_by_id(id):
        """Get check with given id.

        :param id: int - Check id.

        :return: Check object if check was found, and None otherwise.
        """

        try:
            check = Check.objects.get(id=id)
        except:
            return None

        return check

    @staticmethod
    def get_by_user_id(user_id):
        """Get checks by user id.

        :param user_id: int - User id.
        :return: QuerySet of checks for given user id.
        """

        checks = Check.objects.filter(service__server__user__id=user_id)

        return checks

    def to_dict(self):
        """Convert model object to dictionary.

        :return: dict:
                {
                    'id': check id,
                    'name': check name,
                    'plugin_name': plugin name,
                    'target_port': target port,
                    'run_freq': run frequency,
                    'service_id': service id
                }
        """

        return {
            'id': self.id,
            'name': self.name,
            'plugin_name': self.plugin_name,
            'target_port': self.target_port,
            'run_freq': self.run_freq,
            'service_id': self.service.id,
        }
