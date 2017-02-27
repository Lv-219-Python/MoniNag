from django.db import models

from server.models import Server

SERVICE_STATUS_CHOICES = (
    ('', 'Unknown'),
    ('fail', 'Fail'),
    ('ok', 'OK'),
)


class Service(models.Model):
    """Service model class.

    Attributes:
        id (int): autogenerated primary key.
        name (str): service name.
        status (str): service status.
        server (int): foreign key to server which owns service (many-to-one).
    """

    name = models.CharField(default='', max_length=200)
    status = models.CharField(default='', choices=SERVICE_STATUS_CHOICES, max_length=10)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    def update(self, name=None, status=None):
        """Update service data.

        Args:
            name(str, optional): service name. Defaults to None.
            status(str, optional): service status. Defaults to None.
        """

        if name:
            self.name = name
        if status:
            self.status = status

        self.save()

    @staticmethod
    def create(name, server, status=''):
        """Create and add service to database.

        Args:
            name(str): service name.
            status(str, optional): service status. Default empty string.
            server(Server): server instance which will own the service.

        Returns:
            Service: Created service.
        """

        service = Service()

        service.name = name
        service.status = status
        service.server = server

        service.save()

        return service

    @staticmethod
    def get_by_id(id):
        """Get service with given id.

        Args:
            id (int): service id.

        Returns:
            Service: If service was found, and None otherwise.
        """

        try:
            service = Service.objects.get(id=id)
        except Exception as error:
            return None

        return service

    @staticmethod
    def get_by_server(server):
        services = Service.objects.filter(server=server)
        return services

    @staticmethod
    def get_by_user_id(user_id):
        """Get services for given user id.

        Args:
            user_id(int): user id.

        Returns:
            QuerySet<Service>: QuerySet of services.
        """

        services = Service.objects.filter(server__user__id=user_id)

        return services

    @staticmethod
    def get_by_server_id(server_id):
        """Get services for given server id.

        Args:
            server_id(int): server id.

        Returns:
            QuerySet<Service>: QuerySet of services.
        """

        services = Service.objects.filter(server__id=server_id)

        return services

    @staticmethod
    def get_by_statuses(statuses):
        """Get services by statuses.

        Args:
            statuses(collection): service statuses.

        Returns:
            QuerySet<Service>: QuerySet of services.
        """

        services = Service.objects.filter(status__in=statuses)
        return services

    def to_dict(self):
        """Convert model object to dictionary.

        Return:
            dict:
                {
                    'id': id,
                    'name': name,
                    'status': status,
                    'server_id': server.id
                }
        """

        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'server_id': self.server.id
        }

    def __str__(self):
        return 'Service id: {}, name: {}, status: {}'.format(self.id,
                                                             self.name,
                                                             self.status)
