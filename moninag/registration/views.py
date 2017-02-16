from json import loads
from django.contrib import auth as authentication
from django.core.validators import validate_email
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from moninag.settings import DEFAULT_HOST, DEFAULT_FROM_EMAIL
from registration.models import CustomUser
from registration.utils.send_email import send_activation_email, generate_activation_key, send_reset_password_email


def auth(request):
    return render(request, 'registration/login.html')


def activate(request, activation_key):

    user = CustomUser.objects.get(activation_key=activation_key)
    if not user.is_active:
        user.is_active = True
        user.save()
    else:
        return render(request, 'registration/already_activated.html')
    return render(request, 'registration/activate.html')


def login(request):

    if request.method == 'POST':
        data = loads(request.body.decode('utf-8'))
        email = data.get('email').strip().lower()
        password = data.get('password').strip()

        user = authentication.authenticate(username=email, password=password)
        if user:
            if user.is_active:
                authentication.login(request, user)
                return JsonResponse({'success': True, 'message': '/'})
            else:
                # Return a 'disabled account' error message
                return HttpResponse('Account is not active', status=401)

        return HttpResponse('Email and/or password invalid', status=403)

    return HttpResponse(status=400)


def logout(request):
    authentication.logout(request)
    return redirect('/auth/')


def register_user(request):
    if request.method == 'POST':
        json = {
            'error': {},
            'message': {},
            'success': False,
        }

        data = loads(request.body.decode('utf-8'))
        email = data.get('email')

        try:
            validate_email(email)
            try:
                CustomUser.objects.get(email=email)
                json['error'] = "This email is already registered. Please try another"
            except CustomUser.DoesNotExist:
                user = CustomUser()
                user.email, user.first_name, user.second_name = email, data.get(
                    'firstName'), data.get('lastName')
                user.set_password(data.get('password'))
                activation_key = generate_activation_key(email)
                user.activation_key = activation_key

                user.save()
                json['success'] = True
                json['message'] = "Thank you for your time. The confirmation code has been sent to your email. In order to confirm the registration, simply click on the link given in it."

                send_activation_email(
                    DEFAULT_HOST, DEFAULT_FROM_EMAIL, user.email, activation_key)
        except:
            json['error'] = "The email address you've entered has not a valid format"

        return JsonResponse(json)

    return render(request, 'registration/register.html')


def request_password_reset(request):
    if request.method == 'POST':
        json = {
            'error': {},
            'message': {},
            'success': False,
        }

        data = loads(request.body.decode('utf-8'))
        email = data.get('email').strip().lower()

        try:
            validate_email(email)
            try:

                user = CustomUser.objects.get(email=email)

                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)

                send_reset_password_email( DEFAULT_HOST, DEFAULT_FROM_EMAIL, user.email, uidb64, token )

                json['success'] = True
                json['message'] = "An email has been sent to " + user.email +". Please check its inbox to continue reseting password."

            except CustomUser.DoesNotExist:
                json['error'] = "No user is associated with this email address"

        except:
            json['error'] = "The email address you've entered has not a valid format"

        return JsonResponse(json)
    return render(request, 'registration/password_reset.html')


def confirm_password_reset(request, uidb64=None, token=None):
    if request.method == 'POST':
        json = {
            'error': {},
            'message': {},
            'success': False,
        }
        data = loads(request.body.decode('utf-8'))
        uidb64 = data.get('uidb64')
        token = data.get('token')

        assert uidb64 is not None and token is not None
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            new_password = data.get('password')
            user.set_password(new_password)
            user.save()
            json['message'] = "Password has been reset. In 5 seconds you will be redirected to the login page."
            json['success'] = True
            return JsonResponse(json)
        else:
            return HttpResponse('The reset password link is no longer valid.', status=403)

    return render(request, 'registration/password_reset_confirm.html')
