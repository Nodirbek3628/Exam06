from django.urls import path
from .views import players_view

urlpatterns = [
    path('players/', players_view, name='players'),           
    path('players/<int:id>/', players_view, name='player'),  
]
