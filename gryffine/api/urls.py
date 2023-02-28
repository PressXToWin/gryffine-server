from django.urls import path

from .views import api_records

app_name = 'api'

urlpatterns = [
    path('v1/records/', api_records),
]
