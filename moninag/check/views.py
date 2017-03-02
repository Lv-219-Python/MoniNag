import json

from django.http import HttpResponse, JsonResponse
from django.views.generic.base import View

from check.models import Check
from nagplugin.models import NagPlugin
from service.models import Service
from server.models import Server

from utils.validators import validate_dict, validate_subdict


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
                'plugin_id': <nagios plugin id>,
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
                        'plugin_id',
                        'run_freq',
                        'target_port',
                        'service_id'
                        }

        json_response = {}

        check_params = json.loads(request.body.decode('utf-8'))

        if not validate_dict(check_params, REQUIREMENTS):
            json_response['error'] = 'Incorrect JSON format.'
            return JsonResponse(json_response, status=400)

        plugin = NagPlugin.get_by_id(check_params['plugin_id'])

        if not plugin:
            json_response['response'] = 'Plugin with given id was not found.'
            return JsonResponse(json_response, status=404)

        service = Service.get_by_id(check_params['service_id'])

        if not service:
            json_response['response'] = 'Service with given id was not found.'
            return JsonResponse(json_response, status=404)

        if not service.server.user.id == request.user.id:
            return HttpResponse(status=403)

        check = Check.create(name=check_params['name'],
                             plugin=plugin,
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
                               Status 403 if permission denied.
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
        OPTIONAL_REQUIREMENTS = {'name',
                                 'plugin_id',
                                 'run_freq',
                                 'target_port',
                                 'state',
                                 }

        json_response = {}

        check_params = json.loads(request.body.decode('utf-8'))

        if not validate_subdict(check_params, OPTIONAL_REQUIREMENTS):
            json_response['error'] = 'Incorrect JSON format.'
            return JsonResponse(json_response, status=400)

        if 'plugin_id' in check_params:
            plugin = NagPlugin.get_by_id(check_params['plugin_id'])

            if not plugin:
                json_response['response'] = 'Plugin with given id was not found.'
                return JsonResponse(json_response, status=404)

            # Replace 'plugin_id' key with 'plugin' key to unpack in update method
            check_params.pop('plugin_id')
            check_params['plugin'] = plugin

        check = Check.get_by_id(check_id)

        if check:
            if check.service.server.user.id == request.user.id:
                check.update(**check_params)
                json_response['response'] = check.to_dict()
                return JsonResponse(json_response, status=200)
            return HttpResponse(json_response, status=403)

        json_response['error'] = 'Check with given id was not found.'
        return HttpResponse(json_response, status=404)
