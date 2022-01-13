from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.movies_titles, name='movies_titles'),
]
