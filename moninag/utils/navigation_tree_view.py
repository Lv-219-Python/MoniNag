"""This module contains method that get the navigation tree"""

from django.http import JsonResponse

from server.models import Server
from service.models import Service
from check.models import Check


def get_navigation_tree(request): 
    """Handles GET request.

        Return all servers of current user with their services and checks.

        Returns:
            JsonResponse:
                {
                    response: <list of servers>
                }
    """
    
    json_response = {}
    data = []

    servers = Server.get_by_user_id(request.user.id)
    for server in servers:

        services = Service.get_by_server(server)
        server_data = server.to_dict()
        server_data['services'] = []

        for service in services:
            checks = Check.get_by_service(service)
            service_data = service.to_dict()
            service_data['checks'] = []
            for check in checks:
                service_data['checks'].append(check.to_dict())

            server_data['services'].append(service_data)

        data.append(server_data)

    json_response['response'] = data
    return JsonResponse(json_response, status=200)
