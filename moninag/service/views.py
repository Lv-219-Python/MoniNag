import json

from django.http import JsonResponse, HttpResponse
from django.views.generic.base import View

from service.models import Service
from utils.validators import validate_dict


REQUIREMENTS = {'name', 'status', 'server_id'}


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
        """

        json_response = {}

        if service_id:
            # Get service with specified id
            service = Service.get_by_id(service_id)

            if service:
                json_response['response'] = service.to_dict()
                return JsonResponse(json_response, status=200)

            json_response['error'] = 'Service with specified id was not found.'
            return JsonResponse(json_response, status=404)

        # Get all services
        json_response['response'] = [service.to_dict() for service in Service.get()]

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
        """

        json_response = {}

        service_dict = json.loads(request.body.decode('utf-8'))

        if not validate_dict(service_dict, REQUIREMENTS):
            json_response['error'] = 'Incorect JSON format.'
            return JsonResponse(json_response, status=400)

        service = Service.create(**service_dict)

        if service:
            json_response['response'] = service.to_dict()
            return JsonResponse(json_response, status=201)

        json_response['error'] = 'Service was not created.'
        return JsonResponse(json_response, status=400)

    def put(self, request, service_id):
        """Handles PUT request.

        Get service data from PUT request and update service with given id in database.
        In response return updated service or error if service was not updated.

        Args:
            service_id(int): service id.

        Returns:
            JsonResponse:
                {
                    response: <service>
                    or
                    error: <error message>
                }
        """

        json_response = {}

        service_dict = json.loads(request.body.decode('utf-8'))

        if not validate_dict(service_dict, REQUIREMENTS):
            json_response['error'] = 'Incorect JSON format.'
            return JsonResponse(json_response, status=400)

        service_dict['id'] = service_id
        service = Service.update(**service_dict)

        if service:
            json_response['response'] = service.to_dict()
            return JsonResponse(json_response, status=200)

        json_response['error'] = 'Service was not updated.'
        return JsonResponse(json_response, status=400)

    def delete(self, request, service_id):
        """Handles DELETE request.

        Delete service with given id from database.

        Returns:
            HttpResponse: Status 200 for success, 400 otherwise.
        """

        deleted = Service.remove(service_id)

        if deleted:
            return HttpResponse(status=200)

        return HttpResponse(status=400)
