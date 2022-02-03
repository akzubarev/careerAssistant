from django.contrib import admin
from django.urls import path

from apps.scoring import views

urlpatterns = [
    path('', views.form),
]
