from django.http import JsonResponse
from django.views.generic.base import View

from nagplugin.models import NagPlugin


class NagPluginView(View):
    """NagPlugin view handles GET request."""

    def get(self, request):
        """Handles GET request.

        Return all nagios plugins in response.

        Returns:
            JsonResponse:
                {
                    response: <list of nagios plugins>
                }
        """

        json_response = {}

        # Get all nagios plugins
        nagplugins = NagPlugin.get(end=None)
        json_response['response'] = [nagplugin.to_dict() for nagplugin in nagplugins]

        return JsonResponse(json_response, status=200)
