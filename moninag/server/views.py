import json

from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.generic.base import View

from server.models import Server


class ServerView(View):
    """Server view handles GET, POST, PUT, DELETE requests."""

    def get(self, request, server_id=None):
        """
        Handles GET request.

        If server_id is None, return all servers in response,
        otherwise server with given id.
        If server with specified id was not found return error.

        Args:
            server_id(int, optional): server id. Defaults to None.

        Returns:
            JsonResponse in format:
            {
                response: <list of servers>/<server>
                or
                error: <error message>
            }
        """
        json_response = {}
        if server_id is None:
            # Get all servers
            servers = Server.get()
            servers_list = [model_to_dict(server) for server in servers]
            json_response['response'] = servers_list
            return JsonResponse(json_response, status=200)

        # Get server with specified id
        server = Server.get_by_id(server_id)
        if server is None:
            json_response['error'] = 'Server with specified id was not found.'
            return JsonResponse(json_response, status=404)
        json_response['response'] = model_to_dict(server)
        return JsonResponse(json_response, status=200)

    def post(self, request):
        """
        Handles POST request.
        Get server data from POST request and create one in database.
        In response return created server or error if server was not created.
        Returns:
            JsonResponse in format:
            {
                response: <server>
                or
                error: <error message>
            }
        """
        json_response = {}
        server_dict = json.loads(request.body.decode('utf-8'))
        server = Server.create(**server_dict)
        if server is None:
            json_response['error'] = 'Server was not created.'
            return JsonResponse(json_response, status=400)
        json_response['response'] = model_to_dict(server)
        return JsonResponse(json_response, status=201)

    def put(self, request, server_id):
        """Handles PUT request.

        Get server data from PUT request and update server with given id in database.
        In response return updated server or error if server was not updated.

        Args:
            server_id(int): server id.

        Returns:
            JsonResponse in format:
            {
                response: <server>
                or
                error: <error message>
            }
        """
        json_response = {}
        server_dict = json.loads(request.body.decode('utf-8'))
        server_dict['id'] = server_id
        server = Server.update(**server_dict)
        if server is None:
            json_response['error'] = 'Server was not updated.'
            return JsonResponse(json_response, status=400)
        json_response['response'] = model_to_dict(server)
        return JsonResponse(json_response, status=200)

    def delete(self, request, server_id):
        """Handles DELETE request.

        Delete server with given id from database.

        Returns:
            JsonResponse in format:
            {
                response: True/False
                or
                error: <error message>
            }

        """
        json_response = {}
        deleted = Server.delete(server_id)
        if deleted:
            json_response['response'] = True
            return JsonResponse(json_response, status=200)
        json_response['error'] = 'Server was not deleted.'
        return JsonResponse(json_response, status=400)
