from django.urls import path
from .views import scores_view

urlpatterns = [
    path('scores/',scores_view,name='score')
]
