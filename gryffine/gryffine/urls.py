from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('records.urls')),
]
