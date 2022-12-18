from django.urls import path
from vkl import views
  
urlpatterns = [
    path("", views.index),
    path("contacts/", views.contacts),
    path("friend/", views.friend),
]