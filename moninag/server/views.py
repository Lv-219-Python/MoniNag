import json

from django.http import HttpResponse, JsonResponse
from django.views.generic.base import View

from server.models import Server
from utils.validators import validate_dict, validate_subdict

REQUIREMENTS = {'name', 'address', 'state'}


class ServerView(View):
    """Server view handles GET, POST, PUT, DELETE requests."""

    def get(self, request, server_id=None):
        """Handles GET request.

        If server_id is None, return all servers in response,
        otherwise server with given id.
        If server with specified id was not found return error.

        :param server_id: int - server id
        :return: JsonResponse:
                {
                    response: <list of servers>/<servers>
                    or
                    error: <error message>
                }
        """

        json_response = {}

        if not server_id:
            # Get all servers
            servers = Server.get_by_user_id(request.user.id)
            json_response['response'] = [server.to_dict() for server in servers]
            return JsonResponse(json_response, status=200)

        # Get server with specified id
        server = Server.get_by_id(server_id)

        if not server:
            # Server not found
            json_response['error'] = 'Server with specified id was not found.'
            return JsonResponse(json_response, status=404)

        if not server.user.id == request.user.id:
            # Server belongs to another user
            return HttpResponse(status=403)

        json_response['response'] = server.to_dict()
        return JsonResponse(json_response, status=200)

    def post(self, request):
        """Handles POST request.

        Get server data from POST request and create one in database.
        In response return created server or error if server was not created.

        Require JSON with fields:
            {
                'name': <server name>,
                'address': <server address>,
                'state': <server state>,
                'user_id': <user_id>
            }

        :return: JsonResponse:
                {
                    response: <server>
                    or
                    error: <error message>
                }
        """

        json_response = {}

        server_dict = json.loads(request.body.decode('utf-8'))

        if not validate_dict(server_dict, REQUIREMENTS):
            json_response['error'] = 'Incorect JSON format.'
            return JsonResponse(json_response, status=400)

        Server.create(user=request.user, **server_dict)
        return HttpResponse(status=201)

    def put(self, request, server_id):
        """Handles PUT request.

        Get server data from PUT request and update server with given id in database.
        In response return updated server or error if server was not updated.

        :param server_id: server id
        :return: JsonResponse:
                {
                    response: <server>
                    or
                    error: <error message>
                }
        """

        json_response = {}

        server_dict = json.loads(request.body.decode('utf-8'))

        if not validate_subdict(server_dict, REQUIREMENTS):
            json_response['error'] = 'Incorect JSON format.'
            return JsonResponse(json_response, status=400)

        server = Server.get_by_id(server_id)

        if not server:
            # Server does not exist
            json_response['error'] = 'Server was not updated.'
            return JsonResponse(json_response, status=404)

        if not request.user.id == server.user.id:
            # Server does not belong to user
            return HttpResponse(status=403)

        server.update(**server_dict)
        return HttpResponse(status=200)

    def delete(self, request, server_id):
        """Handles DELETE request.

        Delete server with given id from database.

        :param server_id: int - server id
        :return: HttpResponse: Status 200 for success, 400 otherwise.
        """

        server = Server.get_by_id(server_id)

        if not server:
            # Server not found
            return HttpResponse(status=404)

        if not request.user.id == server.user.id:
            # Server does not belong to user
            return HttpResponse(status=403)

        server.delete()
        return HttpResponse(status=200)
