from django.contrib import admin
from .views import RoomView
from django.urls import include, path

urlpatterns = [
    path('room', RoomView.as_view()),
