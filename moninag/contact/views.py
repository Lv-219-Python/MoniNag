"""This module contains contact view with methods for CRUD operations"""

import json

from django.core.validators import validate_email
from django.http import JsonResponse, HttpResponse
from django.views.generic.base import View
from django.shortcuts import render

from contact.models import Contact
from contact.utils.verify_email import send_verification_email
from moninag.settings import DEFAULT_FROM_EMAIL, DEFAULT_HOST
from registration.utils.send_email import generate_activation_key
from utils.validators import validate_dict, validate_subdict

REQUIREMENTS = {
    'first_name',
    'second_name',
    'email'
}


class ContactView(View):
    """Contact view handles GET, POST, PUT, DELETE requests."""

    def get(self, request, contact_id=None):
        """Handles GET request.
        If contact_id is None, return json response with all contacts,
        otherwise contact with given id.
        If contact with specified id was not found return error.
        :param contact_id: int - contact id
        :return: JsonResponse:
                {
                    response: <list of contacts>
                    or
                    error: <error message>
                }
        """
        json_response = {}

        if not contact_id:
            contacts = Contact.get_by_user_id(request.user.id)
            json_response['response'] = [contact.to_dict()
                                         for contact in contacts]
            return JsonResponse(json_response, status=200)

        contact = Contact.get_by_id(contact_id)

        if not contact:
            json_response['error'] = 'Contact with specified id was not found.'
            return JsonResponse(json_response, status=404)

        if not contact.user.id == request.user.id:
            return HttpResponse(status=403)

        json_response['response'] = contact.to_dict()

        return JsonResponse(json_response, status=200)

    def post(self, request):
        """Handles POST request.
        Get contact data from POST request and create one in database.
        In response return created contact or error if contact was not created.
        Require JSON with fields:
            {
                'first_name': <contact first name>,
                'second_name': <contact second name>,
                'email': <contact email>
            }
        :return: JsonResponse:
                {
                    response: <contact>
                    or
                    error: <error message>
                }
        """

        json_response = {}

        contact_params = json.loads(request.body.decode('utf-8'))

        if not validate_dict(contact_params, REQUIREMENTS):
            json_response['error'] = 'Incorrect JSON format.'
            return JsonResponse(json_response, status=400)

        email = contact_params.get('email')

        try:
            validate_email(email)
            try:
                Contact.objects.get(email=email)
                json_response['error'] = 'User with such email is already exists.'
                return JsonResponse(json_response, status=400)

            except Contact.DoesNotExist:
                contact = Contact()

                contact.first_name = contact_params['first_name']
                contact.second_name = contact_params['second_name']
                contact.email = email
                contact.user = request.user
                activation_key = generate_activation_key(email)
                contact.activation_key = activation_key
                contact.save()

                send_verification_email(
                    DEFAULT_HOST, DEFAULT_FROM_EMAIL, contact.email, activation_key)

                json_response['response'] = contact.to_dict()
                return JsonResponse(json_response, status=201)

        except:  # pylint: disable=bare-except
            json_response['error'] = 'Invalid email format.'
            return JsonResponse(json_response, status=400)

    def verify(request, activation_key):  # pylint: disable=no-self-argument
        """Making contact active (active=False -> active=True)"""
        contact = Contact.objects.get(activation_key=activation_key)
        contact.is_active = True
        contact.save()

        return render(request, 'contact/verified.html')

    def put(self, request, contact_id):  # pylint: disable=no-self-use
        """Handles PUT request.
        Get contact data from PUT request and update contact with given id in database.
        In response return updated contact or error if contact was not updated.
        :param contact_id: contact id
        :return: JsonResponse:
                {
                    response: <contact>
                    or
                    error: <error message>
                }
        """

        json_response = {}

        contact_params = json.loads(request.body.decode('utf-8'))

        if not validate_subdict(contact_params, REQUIREMENTS):
            json_response['error'] = 'Incorrect JSON format.'
            return JsonResponse(json_response, status=400)

        email = contact_params.get('email')

        try:
            validate_email(email)

            contact = Contact.get_by_id(contact_id)

            if not contact:
                json_response['error'] = 'Contact was not found.'
                return JsonResponse(json_response, status=404)

            if not request.user.id == contact.user.id:
                return HttpResponse(status=403)

            contact.update(**contact_params)
            json_response['response'] = contact.to_dict()
            return JsonResponse(json_response, status=200)

        except:  # pylint: disable=bare-except
            json_response['error'] = 'Invalid email format.'
            return JsonResponse(json_response, status=400)

    def delete(self, request, contact_id):  # pylint: disable=no-self-use
        """Handles DELETE request.
        Delete contact with given id from database.
        :param contact_id: int - contact id
        :return: HttpResponse: Status 200 for success, 403 otherwise.
        """

        contact = Contact.get_by_id(contact_id)

        if contact:
            if contact.user.id == request.user.id:
                contact.delete()
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=403)

        return HttpResponse(status=404)
