from django.urls import path

from apps.recommendations import views

urlpatterns = [
    path('', views.main),
    path('stub/', views.stub),
]
