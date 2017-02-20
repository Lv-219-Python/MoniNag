import json

from django.core.validators import validate_email
from django.http import JsonResponse, HttpResponse
from django.views.generic.base import View
from django.shortcuts import render

from contact.models import Contact
from moninag.settings import DEFAULT_FROM_EMAIL, DEFAULT_HOST
from utils.validators import validate_dict, validate_subdict
from registration.utils.send_email import generate_activation_key
from contact.utils.verify_email import send_verification_email

REQUIREMENTS = {'first_name',
                'second_name',
                'email'
                }


class ContactView(View):

    def get(self, request, contact_id=None):

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

        except:
            json_response['error'] = 'Invalid email format.'
            return JsonResponse(json_response, status=400)

        return JsonResponse(json_response, status=201)

    def verify(request, activation_key):

        contact = Contact.objects.get(activation_key=activation_key)
        contact.is_active = True
        contact.save()

        return render(request, 'contact/verified.html')

    def put(self, request, contact_id):

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

        except:
            json_response['error'] = 'Invalid email format.'

        return JsonResponse(json_response)

    def delete(self, request, contact_id):

        contact = Contact.get_by_id(contact_id)

        if contact:
            if contact.user.id == request.user.id:
                contact.delete()
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=403)

        return HttpResponse(status=404)
