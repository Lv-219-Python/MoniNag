"""This module contains middleware which performs auth check"""

from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AuthCheckerMiddleware(MiddlewareMixin):  # pylint: disable=too-few-public-methods
    """Auth check middleware which performs user auth check and further redirects"""

    def process_request(self, request):  # pylint: disable=no-self-use
        """Handle requests before view."""

        if request.user.is_authenticated:

            if (request.path_info.startswith('/auth') and not
                request.path_info.startswith('/auth/logout')):

                return redirect("/")
        else:
            if not request.path_info.startswith('/auth'):
                return redirect("auth")

        return None
