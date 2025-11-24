from django.http import HttpRequest,HttpResponse

# Create your views here.
def players_view(request:HttpRequest)->HttpResponse:
    return HttpResponse('players')