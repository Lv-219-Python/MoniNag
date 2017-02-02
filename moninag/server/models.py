from django.db import models

from registration.models import CustomUser

STATE_CHOICES = (
    (1, "NotSelected"),
    (2, "Production"),
    (3, "Staging"),
)


class Server(models.Model):
    """
    Server
    Attributes:
        id:         Integer - AutoField (primary key)
        name:       String - Server name
        address:    String - Server address (ipv4/ipv6/...)
        state:      String - production state (production/staging/...)
        user_id:    Integer - user_id for this server
    """
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=100, choices=STATE_CHOICES, default=0)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    @classmethod
    def create(cls, name, address, state, user):
        """
        Create and add server to database.
        Args:
            name(str): server name.
            address(str): server adress.
            state(str); server state.
            user(int): user id.
        Returns:
            Server: The return value. Created server for success, None otherwise.
        """
        # Will be replaced with appropriate CustomUser method
        user_obj = CustomUser.objects.filter(id=user)
        if len(user_obj) == 1:
            server = cls(name=name, address=address, state=state, user=user_obj[0])
            server.save()
            return server
        return None

    @classmethod
    def update(cls, id, name, address, state, user):
        """
        Update server data.
        Args:
            id(int): server id.
            name(str): server name.
            address(str): server adress.
            state(str); server state.
            user(int): user id.
        Returns:
            Server: The return value. Updated server for success, None otherwise.
        """
        # Check if server exist allready
        if cls.objects.filter(id=id).count() == 1:
            # Will be replaced with appropriate CustomUser method
            user_obj = CustomUser.objects.filter(id=user)
            if len(user_obj) == 1:
                server = cls(id=id, name=name, address=address, state=state, user=user_obj[0])
                server.save()
                return server
            return None

    @classmethod
    def get_by_id(cls, id):
        """
        Get server with given id.
        Args:
            id (int): server id.
        Returns:
            Server: If server was found, and None otherwise.
        """
        server = cls.objects.filter(id=id)
        if len(server) == 1:
            return server[0]
        return None

    @classmethod
    def get(cls, state=None):
        """
        Get servers.
        If state is given it is used as filter,
        otherwise all servers are returned.
        Args:
            state(str, optional): server state. Defaults to None.
        Returns:
            QuerySet<Server>: QuerySet of servers.
        """
        if state is None:
            servers = cls.objects.all()
        else:
            servers = cls.objects.filter(state=state)
        return servers

    @classmethod
    def delete(cls, id):
        """
        Delete server with given id.
        Args:
            id (int): server id.
        Returns:
            bool: The return value. True for success, False otherwise.
        """
        server = cls.objects.filter(id=id)
        if len(server) == 1:
            server.delete()
            return True
        return False

    def __str__(self):
        return "ServerId: {}, ServerName: {}, ServerAddress: {}, ServerState {}".format(self.id,
                                                                                        self.name,
                                                                                        self.address,
                                                                                        self.state)
