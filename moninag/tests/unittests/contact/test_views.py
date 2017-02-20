import json

from django.core.urlresolvers import reverse
from django.test import Client
from django.test import TestCase

from contact.models import Contact
from registration.models import CustomUser


def to_dict(contact):

    return {
        'id': contact.id,
        'first_name': contact.first_name,
        'second_name': contact.second_name,
        'email': contact.email
    }


class ContactViewTest(TestCase):
    def setUp(self):

        self.user = CustomUser.objects.create(
            id=1,
            first_name='Test',
            second_name='User',
            email='test@gmail.com',
            is_active=True)

        self.user.set_password('password')
        self.user.save()

        CustomUser.objects.create(
            id=2,
            first_name='Stephen',
            second_name='Strange',
            email='test2@gmail.com',
            is_active=True)

        Contact.objects.create(
            id=1,
            first_name='first_name1',
            second_name='second_name1',
            email='example1@email.com',
            user=CustomUser.objects.get(id=1))

        Contact.objects.create(
            id=3,
            first_name='first_name3',
            second_name='second_name3',
            email='example3@email.com',
            user=CustomUser.objects.get(id=1))

        Contact.objects.create(
            id=4,
            first_name='4first/name',
            second_name='4second?name',
            email='example4@email.com',
            user=CustomUser.objects.get(id=2))

        self.client = Client()
        self.client.login(username='test@gmail.com', password='password')

    def test_get_contacts(self):

        url = reverse('contacts')
        response = self.client.get(url)

        contacts = Contact.objects.filter(user=1)
        expected_json_response = {}
        expected_json_response['response'] = [to_dict(contact) for contact in contacts]

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content.decode('utf-8'), expected_json_response)

    def test_get_by_contact_id(self):

        url = reverse('contact', args=[1])
        response = self.client.get(url)

        contact = Contact.objects.get(id=1)
        expected_json_response = {}
        expected_json_response['response'] = to_dict(contact)

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content.decode('utf-8'), expected_json_response)

    def test_get_contact_permission_denied(self):

        url = reverse('contact', args=[4])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 403)

    def test_get_not_existing_contact(self):

        url = reverse('contact', args=[10])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_post(self):

        url = reverse('contacts')
        data = json.dumps({'first_name': 'newFirstName',
                           'second_name': 'newSecondName',
                           'email': 'example5@email.com'})

        response = self.client.post(url, data=data, content_type='application/json')
        contact = Contact.objects.get(id=2)

        expected_json_response = {}
        expected_json_response['response'] = to_dict(contact)
        self.assertEqual(response.status_code, 201)
        self.assertJSONEqual(response.content.decode('utf-8'), expected_json_response)

    def test_post_incorrect_format(self):

        url = reverse('contacts')
        data = json.dumps({'first_name': 'newFirstName',
                           'second_name': 'newSecondName'})

        response = self.client.post(url, data=data, content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_put(self):

        url = reverse('contact', args=[1])
        data = json.dumps({'first_name': 'changedFirstName',
                           'second_name': 'changedSecondName',
                           'email': 'changed@email.com'})

        response = self.client.put(url, data=data, content_type='application/json')
        contact = Contact.objects.get(id=1)

        expected_json_response = {}
        expected_json_response['response'] = to_dict(contact)

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content.decode('utf-8'), expected_json_response)

    def test_put_incorrect_format(self):

        url = reverse('contact', args=[1])
        data = json.dumps({'first_name': 'newFirstName',
                           'second_nme': 'newSecondName'})

        response = self.client.put(url, data=data, content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_put_not_existing_contact(self):

        url = reverse('contact', args=[111])
        data = json.dumps({'first_name': 'changedFirstName',
                           'second_name': 'changedSecondName',
                           'email': 'changed@email.com'})

        response = self.client.put(url, data=data, content_type='application/json')

        self.assertEqual(response.status_code, 404)

    def test_put_permission_denied(self):

        url = reverse('contact', args=[4])
        data = json.dumps({'first_name': 'changedFirstName',
                           'second_name': 'changedSecondName',
                           'email': 'changed@email.com'})

        response = self.client.put(url, data=data, content_type='application/json')

        self.assertEqual(response.status_code, 403)

    def test_delete(self):

        url = reverse('contact', args=[1])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Contact.objects.all()), 2)

    def test_delete_permission_denied(self):

        url = reverse('contact', args=[4])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 403)

    def test_delete_not_existing_contact(self):

        url = reverse('contact', args=[44])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 404)
