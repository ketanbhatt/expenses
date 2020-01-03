from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin-app/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
