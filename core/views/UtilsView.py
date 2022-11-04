from django.http import JsonResponse

class UtilsView:

    def validate_len(string, string_len, message):
        if(len(string) < int(string_len)): 
            return JsonResponse({"success": False, "message": str(message)})

