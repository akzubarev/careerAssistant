from django.urls import path

from apps.recomendations import views

urlpatterns = [
    path('', views.main),
    path('stub/', views.stub),
]
