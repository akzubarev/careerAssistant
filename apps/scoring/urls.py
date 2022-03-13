from django.contrib import admin
from django.urls import path

from apps.scoring import views

app_name = "scoring"
urlpatterns = [
    path('', views.form, name="form"),
    path('scoring/', views.scoring, name="scoring"),
    path('processing/', views.processing, name="processing"),
]
