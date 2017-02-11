import json

from django.http import JsonResponse
from django.views.generic.base import View

from registration.models import CustomUser
from utils.validators import validate_subdict


class UserProfileView(View):
    """UserProfileView handles GET, PUT requests."""

    def get(self, request, user_id=None):
        """Handles GET request.

        If user_id is None, return user profile from request in response,
        otherwise user profile with given id.
        If user with specified id was not found return error.

        Args:
            user_id(int, optional): user id. Defaults to None.

        Returns:
            JsonResponse:
                {
                    response: <user profile>
                    or
                    error: <error message>
                }
        """

        json_response = {}

        if not user_id:
            json_response['response'] = request.user.to_dict()
            return JsonResponse(json_response, status=200)

        user = CustomUser.get_by_id(user_id)

        if not user:
            json_response['error'] = 'User with specified id was not found.'
            return JsonResponse(json_response, status=404)

        json_response['response'] = user.to_dict()
        return JsonResponse(json_response, status=200)

    def put(self, request):
        """Handles PUT request.

        Get user data from PUT request and update user from request profile in database.
        In response return updated user profile or error if user profile was not updated.

        Returns:
            JsonResponse:
                {
                    response: <user profile>
                    or
                    error: <error message>
                }
        """

        json_response = {}

        OPTIONAL_REQUIREMENTS = {'first_name', 'second_name'}

        user_params = json.loads(request.body.decode('utf-8'))

        if not validate_subdict(user_params, OPTIONAL_REQUIREMENTS):
            json_response['error'] = 'Incorrect JSON format.'
            return JsonResponse(json_response, status=400)

        request.user.update(**user_params)

        json_response['response'] = request.user.to_dict()
        return JsonResponse(json_response, status=200)

