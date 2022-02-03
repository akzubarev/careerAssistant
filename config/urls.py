from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include('apps.main.urls')),
    path("form/", include('apps.scoring.urls')),
    path("recomend/", include('apps.recommendations.urls')),
    path("profile/", include('apps.users.urls')),
    path('admin/', admin.site.urls),
]
