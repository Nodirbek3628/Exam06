from django.http import HttpRequest,HttpResponse

# Create your views here.
def games_view(requst:HttpRequest)->HttpResponse:
    return HttpResponse('ok')