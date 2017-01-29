from json import loads
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import auth
from django.core.validators import validate_email
from django.template.context_processors import csrf
from moninag.settings import DEFAULT_HOST, DEFAULT_FROM_EMAIL
from registration.utils.send_email import send_activation_email
from registration.forms import CustomUserCreationForm
from registration.models import CustomUser


def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)


def activate(request, activation_key):
    activation_key = int(activation_key)
    user = CustomUser.objects.get(id=activation_key)
    if not user.is_active:
        user.is_active = True
        user.save()
    else:
        return render(request, 'already_activated.html')
    return render(request, 'activate.html')


def auth_view(request):
    json = {
        'error': {},
        'message': {},
        'success': False,
    }

    data = loads(request.body.decode('utf-8'))


    if request.method == 'POST':
        email = data.get('email').strip().lower()
        password = data.get('password').strip()

        user = auth.authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                json['success'] = True
                json['message'] = '/accounts/profile/'
            else:
                # Return a 'disabled account' error message
                json['error'] = 'Account is not active'
        else:
            # Return an 'invalid login' error message.
            json['error'] = 'Email and/or password invalid.'
    return JsonResponse(json)


def inactive_account(request):
    return render(request, 'inactive_account.html')


def profile(request):
    return render(request, 'profile.html',
                  {'user': request.user})


def invalid_login(request):
    return render(request, 'invalid_login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/')


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
                user.save()
                json['success'] = True
                json['message'] = "Thank you for your time. The confirmation code has been sent to your email. In order to confirm the registration, simply click on the link given in it."
                send_activation_email(
                    DEFAULT_HOST, DEFAULT_FROM_EMAIL, user.email, user.id)
        except:
            json['error'] = "The email address you've entered has not a valid format"

        return JsonResponse(json)
    else:
        form = CustomUserCreationForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render(request, 'register.html', args)


def register_success(request):
    return render(request, 'register_success.html')
