from django.urls import path
from .views import players_view

urlpatterns = [
    path('players/',players_view,name='player')
]
