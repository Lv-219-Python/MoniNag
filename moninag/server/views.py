import json

from django.http import JsonResponse, HttpResponse
from django.views.generic.base import View

from server.models import Service

class ServerView(View):
    """Service view handles GET, POST, PUT, DELETE requests."""

    def get(self, request, server_id=None):
        """Handles GET request.

        If service_id is None, return all services in response,
        otherwise service with given id.
        If service with specified id was not found return error.

        Args:
            service_id(int, optional): service id. Defaults to None.

        Returns:
            JsonResponse:
                {
                    response: <list of services>/<service>
                    or
                    error: <error message>
                }
        """

        json_response = {}

        if server_id:
            # Get service with specified id
            server = Server.get_by_id(server_id)

            if server:
                json_response['response'] = server.to_dict()
                return JsonResponse(json_response, status=200)

            json_response['error'] = 'Server with specified id was not found.'
            return JsonResponse(json_response, status=404)

        # Get all services
        json_response['response'] = [server.to_dict() for server in Server.get()]

        return JsonResponse(json_response, status=200)
