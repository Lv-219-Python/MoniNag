from django.shortcuts import render
from registration.models import CustomUser
from django.http import HttpResponse


def profile(request, id):
    try:
        user = CustomUser.objects.get(pk=id)
        if user.is_active:
            if request.user.is_authenticated:
                return render(request, 'user_profile/profile.html', {'user': user})
        return HttpResponse('Account is not active', status=401)
    except CustomUser.DoesNotExist:
        return HttpResponse('Email and/or password invalid', status=403)
