from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index.html"),
    path("add/", views.index, name="index.html")
]
