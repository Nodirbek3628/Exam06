from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
def scores_view(request:HttpRequest)->HttpResponse:
    return HttpResponse('scores')