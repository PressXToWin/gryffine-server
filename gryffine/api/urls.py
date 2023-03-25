from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RecordViewSet

app_name = 'api'

v1_router = DefaultRouter()
v1_router.register('records', RecordViewSet, basename='records')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
