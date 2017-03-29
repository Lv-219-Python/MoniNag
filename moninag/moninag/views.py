from django.shortcuts import render_to_response


def error_404(request):
    return render_to_response('404.html')
