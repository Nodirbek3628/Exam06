from django.urls import path
from .views import Game_view

urlpatterns = [
    path('games/', Game_view.as_view(), name='games'),
    path('games/<int:id>/', Game_view.as_view(), name='game_detail'),
]
