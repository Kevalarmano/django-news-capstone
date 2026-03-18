from django.http import JsonResponse

def news_list(request):
    return JsonResponse({"message": "News API working"})