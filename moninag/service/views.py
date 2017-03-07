"""This module contains Service view with methods for CRUD operations"""

import json

from django.http import HttpResponse, JsonResponse
from django.views.generic.base import View

from check.models import Check
from server.models import Server
from service.models import Service
from utils.validators import validate_dict, validate_subdict


class ServiceView(View):
    """Service view handles GET, POST, PUT, DELETE requests."""

    def get(self, request, service_id=None):
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
            or
            HttpResponse: status 403 if service does not belong to user.
        """

        json_response = {}

        if not service_id:
            # Get all services of user
            user_services = Service.get_by_user_id(request.user.id)
            json_response['response'] = [service.to_dict() for service in user_services]

            return JsonResponse(json_response, status=200)

        # Get service with specified id
        service = Service.get_by_id(service_id)

        if not service:
            json_response['error'] = 'Service with specified id was not found.'
            return JsonResponse(json_response, status=404)

        if not request.user.id == service.server.user.id:
            return HttpResponse(status=403)

        checks = Check.get_by_service(service)
        data = service.to_dict()
        data['checks'] = [
            {
                'id': check.id,
                'name': check.name,
                'plugin_id': check.plugin.id,
                'plugin_name': check.plugin.name,
                'status': check.status,
                'state': check.state,
            } for check in checks]

        json_response['response'] = data

        return JsonResponse(json_response, status=200)

    def post(self, request):
        """Handles POST request.

        Get service data from POST request and create one in database.
        In response return created service or error if service was not created.

        Require JSON with fields:
            {
                'name': <service name>,
                'status': <service status>,
                'server_id': <server_id>
            }

        Returns:
            JsonResponse:
                {
                    response: <service>
                    or
                    error: <error message>
                }
            or
            HttpResponse: status 403 if server does not belong to user.
        """

        json_response = {}

        requirements = {'name', 'status', 'server_id'}

        service_params = json.loads(request.body.decode('utf-8'))

        if not validate_dict(service_params, requirements):
            json_response['error'] = 'Incorrect JSON format.'
            return JsonResponse(json_response, status=400)

        server = Server.get_by_id(server_id=service_params['server_id'])

        if not server:
            json_response['error'] = 'Server with given id was not found.'
            return JsonResponse(json_response, status=404)

        if not server.user.id == request.user.id:
            return HttpResponse(status=403)

        service = Service.create(name=service_params['name'],
                                 status=service_params['status'],
                                 server=server)

        json_response['response'] = service.to_dict()
        return JsonResponse(json_response, status=201)

    def put(self, request, service_id):  # pylint: disable=no-self-use
        """Handles PUT request.

        Get service data from PUT request and update service with given id in database.
        In response return updated service or error if service was not updated.

        Args:
            service_id(int): service id.

        Except JSON with fields:
            {
                'name': <service name>,
                'status': <service status>
            }

        Returns:
            JsonResponse:
                {
                    response: <service>
                    or
                    error: <error message>
                }
            or
            HttpResponse: status 403 if service does not belong to user.
        """

        json_response = {}

        optional_requirements = {'name', 'status'}

        service_params = json.loads(request.body.decode('utf-8'))

        if not validate_subdict(service_params, optional_requirements):
            json_response['error'] = 'Incorrect JSON format.'
            return JsonResponse(json_response, status=400)

        service = Service.get_by_id(service_id)

        if not service:
            json_response['error'] = 'Service with given id was not found.'
            return JsonResponse(json_response, status=404)

        if not request.user.id == service.server.user.id:
            return HttpResponse(status=403)

        service.update(**service_params)

        json_response['response'] = service.to_dict()
        return JsonResponse(json_response, status=200)

    def delete(self, request, service_id): # pylint: disable=no-self-use
        """Handles DELETE request.

        Delete service with given id from database.

        Returns:
            HttpResponse: Status 200 for success,
                403 if service does not belong to user,
                404 if service not found.
        """

        service = Service.get_by_id(service_id)

        if not service:
            return HttpResponse(status=404)

        if not request.user.id == service.server.user.id:
            return HttpResponse(status=403)

        service.delete()

        return HttpResponse(status=200)
