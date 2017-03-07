import json

from django.core.urlresolvers import reverse
from django.test import TestCase, Client, mock

from registration.models import CustomUser


def mock_uidb64(self):
    """ Mock uidb64 for password reset"""
    # pylint: disable=unused-argument

    return '1000'


class FakeToken(object):
    """ Mock token for password reset"""
    # pylint: disable=too-few-public-methods

    def __init__(self, *args, **kwargs):
        pass

    def check_token(self, a):
        # pylint: disable=unused-argument, invalid-name, no-self-use, missing-docstring
        return True


class LoginViewTest(TestCase):
    # pylint: disable=missing-docstring

    def setUp(self):
        self.user = CustomUser.objects.create(id=1000,
                                              first_name='FirstName',
                                              second_name='SecondName',
                                              email='testmail@test.so',
                                              avatar='avatartest',
                                              activation_key='testkey',
                                              is_active=True)

        self.user.set_password('rootroot')
        self.user.save()
        self.client = Client()

    def test_auth(self):
        """Ensure we can access the login html"""

        url = reverse('auth')
        response = self.client.get(url)
        expected = 'registration/login.html'

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, expected)

    def test_activate(self):
        """Ensure that activate() method works properly"""

        user = CustomUser.objects.get(email='testmail@test.so')
        user.is_active = False
        user.save()

        url = reverse('activate', args=['testkey'])
        response = self.client.get(url)
        user = CustomUser.objects.get(email='testmail@test.so')
        expected = 'registration/activate.html'

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, expected)
        self.assertEqual(user.is_active, True)

    def test_already_activated(self):
        """Ensure that activate() method works properly,
           if user is already activated"""

        user = CustomUser.objects.get(email='testmail@test.so')
        url = reverse('activate', args=['testkey'])
        response = self.client.get(url)
        expected = 'registration/already_activated.html'

        self.assertEqual(user.is_active, True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, expected)

    def test_login(self):
        """Ensure that login() method works properly"""

        user_data = json.dumps({'email': 'testmail@test.so',
                                'password': 'rootroot',
                               })
        url = reverse('login')
        response = self.client.post(url, data=user_data, content_type='application/json')

        self.assertEqual(response.status_code, 200)

    def test_login_is_not_active(self):
        """Ensure we get 401 response if user is not active"""

        self.user.is_active = False
        self.user.save()
        user_data = json.dumps({'email': 'testmail@test.so',
                                'password': 'rootroot'})

        url = reverse('login')
        response = self.client.post(url, data=user_data, content_type='application/json')

        self.assertEqual(response.status_code, 401)

    def test_login_invalid_email_password(self):
        """Ensure we can't log in with invalid email/password"""

        user_data = json.dumps({'email': 'abyrvalg',
                                'password': 'glavryba'})

        url = reverse('login')
        response = self.client.post(url, data=user_data, content_type='application/json')

        self.assertEqual(response.status_code, 403)

    def test_login_method_GET(self):
        """Ensure we get a right response when using !=POST method"""

        url = reverse('login')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 400)

    def test_logout(self):
        """Ensure we can successfully log out."""

        self.client.login(username='testmail@test.so', password='rootroot')
        urllogout = reverse('logout')
        response_out = self.client.get(urllogout)

        self.assertRedirects(response_out, '/auth/',
                             status_code=302, target_status_code=200)

    def test_register_user(self):
        """Ensure that we can successfully register a user."""

        reg_data = json.dumps({'email': 'testmail2@test.so',
                               'firstName': 'TestName',
                               'lastName': 'LastName',
                               'password': 'isecretlyloveunittests'})

        url = reverse('register_user')
        response = self.client.post(url, data=reg_data, content_type='application/json')
        expected = json.dumps({'error': {},
                               'message': 'Thank you for your time. '
                                          'The confirmation code has been sent to your email. '
                                          'In order to confirm the registration, simply click on '
                                          'the link given in it.',
                               'success': True})

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), expected)

    def test_register_user_get(self):
        """Test if we get right render with GET method"""

        url = reverse('register_user')
        response_render = self.client.get(url)

        self.assertTemplateUsed(response_render, 'registration/register.html')

    def test_already_registered_email(self):
        """Ensure that we get an error when we try
           to register with an already registered email"""
        new_reg_data = json.dumps({'email': 'testmail@test.so',
                                   'firstName': 'Iam',
                                   'lastName': 'Inlove',
                                   'password': 'withunittests'})

        expected_json = json.dumps({'error': 'This email is already registered. '
                                             'Please try another',
                                    'message': {},
                                    'success': False})

        url = reverse('register_user')
        response = self.client.post(url, data=new_reg_data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), expected_json)

    def test_registration_invalid_email(self):
        """Ensure we can't register with invalid email"""

        reg_data = json.dumps({'email': 'invalid',
                               'firstName': 'TestName',
                               'lastName': 'LastName',
                               'password': 'isecretlyloveunittests'})

        expected_json = json.dumps({'error': "The email address you've entered "
                                             "has not a valid format",
                                    'message': {},
                                    'success': False})

        url = reverse('register_user')
        response = self.client.post(url, data=reg_data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), expected_json)

    def test_request_password_reset(self):
        """Ensure that user can reset his password"""

        reg_data = json.dumps({'email': 'testmail@test.so'})
        expected = json.dumps({'error': {},
                               'message': 'An email has been sent to testmail@test.so. '
                                          'Please check its inbox to continue reseting password.',
                               'success': True})

        url = reverse('reset_password')
        response = self.client.post(url, data=reg_data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), expected)

    def test_request_password_reset_nonexisting_user(self):
        """Ensure we can't send an email if it is
           not connected to some user"""

        reg_data = json.dumps({'email': 'nonexistant@test.so'})
        expected_json = json.dumps({'error': 'No user is associated with this email address',
                                    'message': {},
                                    'success': False})

        url = reverse('reset_password')
        response = self.client.post(url, data=reg_data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), expected_json)

    def test_request_password_reset_method_GET(self):
        """Ensure that method GET renders the right page"""

        url = reverse('reset_password')
        response_render = self.client.get(url)
        expected = 'registration/password_reset.html'

        self.assertTemplateUsed(response_render, expected)

    def test_request_password_reset_invalid_email(self):
        """Ensure that user can't reset password with invalid email"""

        reg_data = json.dumps({'email': 'invalid'})
        expected = json.dumps({'error': "The email address you've entered has not a valid format",
                               'message': {},
                               'success': False})

        url = reverse('reset_password')
        response = self.client.post(url, data=reg_data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), expected)

    @mock.patch('registration.views.urlsafe_base64_decode', mock_uidb64)
    @mock.patch('registration.views.default_token_generator', FakeToken)
    def test_confirm_password_reset(self):
        """Ensure we can confirm the password reset"""

        reg_data = json.dumps({'uidb64': '1000',
                               'token': 'mocktoken',
                               'password': 'testpass'})

        url = reverse('confirm_password_reset', args=['1000', 'mocktoken'])
        response = self.client.post(url, data=reg_data, content_type='application/json')
        expected = ({'error': {},
                     'message': 'Password has been reset. '
                                'In 5 seconds you will be redirected to the login page.',
                     'success': True})

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), expected)

    def test_confirm_password_reset_link_unavailable(self):
        """Ensure we get an error when trying to confirm
           the reset with unworking link"""

        reg_data = json.dumps({'uidb64': '1000',
                               'token': 'mocktoken',
                               'password': 'testpass'})

        url = reverse('confirm_password_reset', args=['wrong', 'wrong'])
        response = self.client.post(url, data=reg_data, content_type='application/json')
        expected = b'The reset password link is no longer valid.'

        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.content, expected)

    def test_confirm_password_reset_not_post(self):
        """Ensure that method GET renders the right page"""

        url = reverse('confirm_password_reset', args=['a', 'b'])
        response = self.client.get(url)
        expected = 'registration/password_reset_confirm.html'

        self.assertTemplateUsed(response, expected)
