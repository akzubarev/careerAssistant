from django.urls import path

from apps.recommendations import views

app_name = "recommendations"
urlpatterns = [
    path('', views.recommendation, name="recommendations"),
]
