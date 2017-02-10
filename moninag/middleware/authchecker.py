from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AuthCheckerMiddleware(MiddlewareMixin):

    def process_request(self, request):
        """Handle requests before view."""

        if request.user.is_authenticated:

            if (request.path_info.startswith('/auth') and not
                request.path_info.startswith('/auth/logout')):

                return redirect("/")
        else:
            if not request.path_info.startswith('/auth'):
                return redirect("auth")

        return None
