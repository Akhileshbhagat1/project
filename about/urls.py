from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_user, name='about_user'),
]