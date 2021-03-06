from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include('apps.main.urls')),
    path("scoring/", include('apps.scoring.urls')),
    path("recommend/", include('apps.recommendations.urls')),
    path("profile/", include('apps.users.urls')),
    path('admin/', admin.site.urls),
]
