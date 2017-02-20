import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from contact.models import Contact
from utils.validators import validate_dict, validate_subdict


REQUIREMENTS = {'first_name',
                'second_name',
                'email'
                }


class ContactView(View):

    def get(self, request, contact_id=None):

        json_response = {}

        if not contact_id:

            contacts = Contact.get_by_user_id(request.user.id)
            json_response['response'] = [contact.to_dict() for contact in contacts]
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
            json_response['error'] = 'Incorect JSON format.'
            return JsonResponse(json_response, status=400)

        contact = Contact.create(first_name=contact_params['first_name'],
                                 second_name=contact_params['second_name'],
                                 email=contact_params['email'].strip().lower(),
                                 user=request.user)

        json_response['response'] = contact.to_dict()
        return JsonResponse(json_response, status=201)

    def put(self, request, contact_id):

        json_response = {}

        contact_params = json.loads(request.body.decode('utf-8'))

        if not validate_subdict(contact_params, REQUIREMENTS):
            json_response['error'] = 'Incorect JSON format.'    
            return JsonResponse(json_response, status=400)

        contact = Contact.get_by_id(contact_id)

        if not contact:
            json_response['error'] = 'Contact was not found.'
            return JsonResponse(json_response, status=404)

        if not request.user.id == contact.user.id:
            return HttpResponse(status=403)

        contact.update(**contact_params)
        json_response['response'] = contact.to_dict()
        return JsonResponse(json_response, status=200)

    def delete(self, request, contact_id):

        contact = Contact.get_by_id(contact_id)

        if contact:
            if contact.user.id == request.user.id:
                contact.delete()
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=403)

        return HttpResponse(status=404)

