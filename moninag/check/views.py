import json

from django.http import JsonResponse, HttpResponse
from django.views.generic.base import View
from utils.validators import validate_dict, validate_subdict

from service.models import Service
from .models import Check


class CheckView(View):

    """Check view handles GET, POST, PUT, DELETE requests."""

    def get(self, request, check_id=None):
        """Handles GET request.

        If check_id is None, return all services in response,
        otherwise check with given id.
        If check with specified id was not found return error.

        :param check_id: int - Check id. Default is None.

        :return: JsonResponse:
                {
                    response: <list of checks>/<check>
                    or
                    error: <error message>
                }
        """

        json_response = {}

        if not check_id:

            user_checks = Check.get_by_user_id(request.user.id)
            json_response['response'] = [check.to_dict() for check in user_checks]

            return JsonResponse(json_response, status=200)

        check = Check.get_by_id(check_id)

        if not check:
            json_response['error'] = 'Check with specified id was not found.'
            return JsonResponse(json_response, status=404)

        if check.service.server.user.id == request.user.id:
            json_response['response'] = check.to_dict()
            return JsonResponse(json_response, status=200)
        else:
            return HttpResponse(status=403)

    def post(self, request):
        """Handles POST request.

        Get check data from POST request and create one in database.
        In response return created check or error if check was not created.

        Require JSON with fields:
            {
                'name': <check name>,
                'plugin_name': <plugin name>,
                'target_port': <target port>,
                'run_freq': <run freq>,
                'service_id': <service id>
            }

        :return: JsonResponse:
                {
                    response: <check>
                    or
                    error: <error message>
                }
        """
        REQUIREMENTS = {'name',
                        'plugin_name',
                        'run_freq',
                        'target_port',
                        'service_id'
                        }

        json_response = {}

        check_params = json.loads(request.body.decode('utf-8'))

        if not validate_dict(check_params, REQUIREMENTS):
            json_response['error'] = 'Incorect JSON format.'
            return JsonResponse(json_response, status=400)

        service = Service.get_by_id(id=check_params['service_id'])

        if not service:
            json_response['response'] = 'Service with given id was not found.'
            return JsonResponse(json_response, status=404)

        if not service.server.user.id == request.user.id:
            return HttpResponse(status=403)

        check = Check.create(name=check_params['name'],
                             plugin_name=check_params['plugin_name'],
                             run_freq=check_params['run_freq'],
                             target_port=check_params['target_port'],
                             service=service)

        json_response['response'] = check.to_dict()
        return JsonResponse(json_response, status=200)

    def delete(self, request, check_id):
        """Handles DELETE request.

        Delete check with given id from database.

        :return: HttpResponse: Status 200 for success,
                               Status 404 if not founded,
                               Status 403 if Unauthorized.
        """

        check = Check.get_by_id(check_id)

        if check:
            if check.service.server.user.id == request.user.id:
                check.delete()
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=403)

        return HttpResponse(status=404)

    def put(self, request, check_id):
        """Handles PUT request.

        Get check data from PUT request and update check with given id in database.
        In response return updated check or error if check was not updated.

        :param check_id: int - Check id.

        :return: JsonResponse:
                {
                    response: <check>
                    or
                    error: <error message>
                }
        """
        REQUIREMENTS = {'name',
                        'plugin_name',
                        'run_freq',
                        'target_port'
                        }

        json_response = {}

        check_dict = json.loads(request.body.decode('utf-8'))

        if not validate_subdict(check_dict, REQUIREMENTS):
            json_response['error'] = 'Incorect JSON format.'
            return JsonResponse(json_response, status=400)

        check = Check.get_by_id(check_id)

        if check:
            if check.service.server.user.id == request.user.id:
                check.update(**check_dict)
                json_response['response'] = check.to_dict()
                return JsonResponse(json_response, status=200)
            return HttpResponse(json_response, status=403)

        json_response['error'] = 'Check with given id was not found.'
        return HttpResponse(json_response, status=404)
