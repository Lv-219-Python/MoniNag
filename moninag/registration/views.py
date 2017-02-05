from json import loads
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib import auth as authentication
from django.core.validators import validate_email
from django.template.context_processors import csrf
from moninag.settings import DEFAULT_HOST, DEFAULT_FROM_EMAIL
from registration.utils.send_email import send_activation_email, generate_activation_key
from registration.models import CustomUser


def auth(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'registration/login.html', c)


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
                return JsonResponse({'success': True, 'message': 'accounts/profile'})
            else:
                # Return a 'disabled account' error message
                return HttpResponse('Account is not active', status=401)

        return HttpResponse('Email and/or password invalid', status=403)

    return HttpResponse(status=400)


def inactive_account(request):
    return render(request, 'registration/inactive_account.html')


def profile(request):
    return render(request, 'registration/profile.html',
                  {'user': request.user})


def invalid_login(request):
    return render(request, 'registration/invalid_login.html')


def logout(request):
    authentication.logout(request)
    return redirect('/accounts/')


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


def register_success(request):
    return render(request, 'registration/register_success.html')
