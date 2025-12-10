from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Event Management API Running"})