"""This module contains Unit Tests for Contact app views"""

import json

from django.core.urlresolvers import reverse
from django.test import Client
from django.test import TestCase

from contact.models import Contact
from registration.models import CustomUser


def to_dict(contact):
    """Convert model object to dictionary.
            :return: dict:
                    {
                        'id': contact id,
                        'first_name': first name,
                        'second_name': second name,
                        'email': email,
                        'is_active': contact status.
                    }
    """

    return {
        'id': contact.id,
        'first_name': contact.first_name,
        'second_name': contact.second_name,
        'email': contact.email,
        'is_active': contact.is_active
    }


class ContactViewTest(TestCase):
    """Tests for Contact model"""

    def setUp(self):
        self.user = CustomUser.objects.create(
            id=1,
            first_name='Test',
            second_name='User',
            email='test@gmail.com',
            is_active=True,
        )

        self.user.set_password('password')
        self.user.save()

        CustomUser.objects.create(
            id=2,
            first_name='Stephen',
            second_name='Strange',
            email='test2@gmail.com',
            is_active=True,
        )

        Contact.objects.create(
            id=101,
            first_name='first_name1',
            second_name='second_name1',
            email='example1@email.com',
            activation_key='activkey',
            user=CustomUser.objects.get(id=1)
        )

        Contact.objects.create(
            id=102,
            first_name='first_name3',
            second_name='second_name3',
            email='example3@email.com',
            is_active=False,
            user=CustomUser.objects.get(id=1)
        )

        Contact.objects.create(
            id=103,
            first_name='4first/name',
            second_name='4second?name',
            email='example4@email.com',
            user=CustomUser.objects.get(id=2)
        )

        self.client = Client()
        self.client.login(username='test@gmail.com', password='password')

    def test_get_contacts(self):
        """Ensure that GET method returns contacts and 200 status."""

        url = reverse('contacts')
        response = self.client.get(url)

        contacts = Contact.objects.filter(user=1)
        expected_json_response = {}
        expected_json_response['response'] = [to_dict(contact) for contact in contacts]

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content.decode('utf-8'), json.dumps(expected_json_response))

    def test_get_by_contact_id(self):
        """Ensure that GET method returns contact with given id and 200 status."""

        url = reverse('contact', args=[101])
        response = self.client.get(url)

        contact = Contact.objects.get(id=101)
        expected_json_response = {}
        expected_json_response['response'] = contact.to_dict()

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content.decode('utf-8'), json.dumps(expected_json_response))

    def test_get_contact_permission_denied(self):
        """Ensure that GET method returns 403 status."""

        url = reverse('contact', args=[103])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 403)

    def test_get_not_existing_contact(self):
        """Ensure that GET method returns error if contact id does not exist and 404 status."""

        url = reverse('contact', args=[10])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_post(self):
        """Ensure that POST method creates contact with specified data and 201 status"""

        url = reverse('contacts')
        data = json.dumps({'first_name': 'test_first_name',
                           'second_name': 'test_second_name',
                           'email': 'test@test.test'})

        response = self.client.post(url, data=data, content_type='application/json')
        contact = Contact.objects.get(id=1)

        expected_json_response = {}
        expected_json_response['response'] = contact.to_dict()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(contact.first_name, 'test_first_name')
        self.assertEqual(contact.second_name, 'test_second_name')
        self.assertEqual(contact.email, 'test@test.test')

        self.assertJSONEqual(response.content.decode('utf-8'), json.dumps(expected_json_response))

    def test_post_incorrect_format(self):
        """Ensure that POST fails to create contact and returns 400 status"""

        url = reverse('contacts')
        data = json.dumps({'first_name': 'test_first_name',
                           'second_name': 'test_second_name'})

        response = self.client.post(url, data=data, content_type='application/json')

        expected_json_response = {}
        expected_json_response['error'] = 'Incorrect JSON format.'

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content.decode('utf-8'), json.dumps(expected_json_response))

    def test_post_existing_email(self):
        """Ensure that POST fails to create contact with existing email and returns 400 status"""

        url = reverse('contacts')
        data = json.dumps({'first_name': 'test_first_name',
                           'second_name': 'test_second_name',
                           'email': 'example1@email.com'})

        response = self.client.post(url, data=data, content_type='application/json')

        expected_json_response = {}
        expected_json_response['error'] = 'User with such email already exists.'

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content.decode('utf-8'), json.dumps(expected_json_response))

    def test_post_invalid_email(self):
        """Ensure that POST fails to create contact with invalid email and returns 400 status"""

        url = reverse('contacts')
        data = json.dumps({'first_name': 'test_first_name',
                           'second_name': 'test_second_name',
                           'email': 'invalid-email.com'})

        response = self.client.post(url, data=data, content_type='application/json')

        expected_json_response = {}
        expected_json_response['error'] = 'Invalid email format.'

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content.decode('utf-8'), json.dumps(expected_json_response))

    def test_verify(self):
        """Ensure that GET method returns expected url and 200 status."""

        contact = Contact.objects.get(id=101)
        contact.is_active = True
        contact.save()

        url = reverse('verify', args=[contact.activation_key])
        response = self.client.get(url)

        expected = 'contact/verified.html'

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, expected)

    def test_put(self):
        """Ensure that PUT method returns fully updated contact and 200 status."""

        url = reverse('contact', args=[102])
        data = json.dumps({'first_name': 'changedFirstName',
                           'second_name': 'changedSecondName',
                           'email': 'changed@email.com'})

        response = self.client.put(url, data=data, content_type='application/json')
        contact = Contact.objects.get(id=102)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(contact.first_name, 'changedFirstName')
        self.assertEqual(contact.second_name, 'changedSecondName')
        self.assertEqual(contact.email, 'changed@email.com')

        expected_json_response = {}
        expected_json_response['response'] = contact.to_dict()

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content.decode('utf-8'), json.dumps(expected_json_response))

    def test_put_invalid_field(self):
        """Ensure that PUT method returns error and 400 status."""

        url = reverse('contact', args=[101])
        data = json.dumps({'first_name': 'newFirstName',
                           'secon_name': 'newSecondName'})

        response = self.client.put(url, data=data, content_type='application/json')

        expected_json_response = {}
        expected_json_response['error'] = 'Incorrect JSON format.'

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content.decode('utf-8'), json.dumps(expected_json_response))

    def test_put_without_email_field(self):
        """Ensure that PUT method edits contact and returns 200 status."""

        url = reverse('contact', args=[101])
        data = json.dumps({'first_name': 'newFirstName',
                           'second_name': 'newSecondName'})

        response = self.client.put(url, data=data, content_type='application/json')
        contact = Contact.objects.get(id=101)

        expected_json_response = {}
        expected_json_response['response'] = contact.to_dict()

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content.decode('utf-8'), json.dumps(expected_json_response))

    def test_put_invalid_email(self):
        """Ensure that PUT fails to edit contact with invalid email and returns 400 status"""

        url = reverse('contact', args=[101])
        data = json.dumps({'email': 'invalid-email.com'})

        response = self.client.put(url, data=data, content_type='application/json')

        expected_json_response = {}
        expected_json_response['error'] = 'Invalid email format.'

        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content.decode('utf-8'), json.dumps(expected_json_response))

    def test_put_not_existing_contact(self):
        """Ensure that PUT method returns error if contact id does not exist and 404 status."""

        url = reverse('contact', args=[111])
        data = json.dumps({'first_name': 'changedFirstName',
                           'second_name': 'changedSecondName'})

        response = self.client.put(url, data=data, content_type='application/json')

        self.assertEqual(response.status_code, 404)

    def test_put_permission_denied_email(self):
        """Ensure that PUT method returns 403 status."""

        url = reverse('contact', args=[103])
        data = json.dumps({'first_name': 'changedFirstName',
                           'second_name': 'changedSecondName',
                           'email': 'changed@email.com'})

        response = self.client.put(url, data=data, content_type='application/json')

        self.assertEqual(response.status_code, 403)

    def test_put_permission_denied(self):
        """Ensure that PUT method returns 403 status."""

        url = reverse('contact', args=[103])
        data = json.dumps({'first_name': 'changedFirstName',
                           'second_name': 'changedSecondName'})

        response = self.client.put(url, data=data, content_type='application/json')

        self.assertEqual(response.status_code, 403)

    def test_delete(self):
        """Ensure that DELETE method returns all contacts for curent user and 200 status."""

        url = reverse('contact', args=[101])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Contact.objects.all()), 2)

    def test_delete_permission_denied(self):
        """Ensure that DELETE method returns 403 status."""

        url = reverse('contact', args=[103])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 403)

    def test_delete_not_existing_contact(self):
        """Ensure that DELETE method returns error if contact id does not exist and 404 status."""

        url = reverse('contact', args=[44])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 404)
