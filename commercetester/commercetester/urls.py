from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('glasses/', include('glasses.urls')),
    path('admin/', admin.site.urls),
]
