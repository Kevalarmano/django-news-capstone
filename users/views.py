from django.http import JsonResponse

def user_list(request):
    data = {
        "message": "Users API working"
    }
    return JsonResponse(data)