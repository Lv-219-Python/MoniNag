from django.shortcuts import render_to_response
from django.views.generic.base import View


class IndexView(View):
    """
    View of the index (home) page
    """

    def get(self, request):
        return render_to_response('index.html')
