"""This module contains View for initial landing home page"""

from django.shortcuts import render_to_response
from django.views.generic.base import View


class IndexView(View):
    """
    View of the index (home) page
    """

    def get(self, request):
        """Method which renders main index page"""

        return render_to_response('index.html')
