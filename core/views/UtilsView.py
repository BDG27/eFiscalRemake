from django.http import JsonResponse
from django.conf import settings

class UtilsView:

    def CEO():
        return {
            "CEO": {
                "pageTitle": settings.CEO_APP_NAME
            }
        }

    def validate_len(string, string_len, message):
        if(len(string) < int(string_len)): 
            return JsonResponse({"success": False, "message": str(message)})

