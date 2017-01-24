from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from moninag.settings import DEFAULT_FROM_EMAIL, DEFAULT_HOST
from registration.forms import CustomUserCreationForm
from registration.models import CustomUser
from registration.utils.send_email import send_activation_email

def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)

def activate(request, activation_key):
    activation_key = int(activation_key)
    user = CustomUser.objects.get(id = activation_key)
    if not user.is_active:
        user.is_active=True
        user.save()
    else:
        return render(request, 'already_activated.html')
    return render(request, 'activate.html')

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/accounts/profile')
        else:
            return HttpResponseRedirect('/accounts/inactive_account', {'active': user.is_active})
    else:
        return HttpResponseRedirect('/accounts/invalid')

def inactive_account(request):
    return render(request, 'inactive_account.html')

def profile(request):
    return render(request, 'profile.html',
                  {'user': request.user })

def invalid_login(request):
    return render(request, 'invalid_login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')

def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            username = request.POST['email']
            password = request.POST['password1']
            user = auth.authenticate(username=username,password=password)
            #The user is not active until they activate their account through email
            user.is_active = False
            user_id = user.id
            email = user.email
            user.save()
            send_activation_email(DEFAULT_HOST, DEFAULT_FROM_EMAIL, email, user_id)
            return HttpResponseRedirect('/accounts/register_success')
    else:
        form = CustomUserCreationForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render(request, 'register.html', args)

def register_success(request):
    return render(request, 'register_success.html')
