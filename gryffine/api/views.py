import ipaddress
import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RecordSerializer


@api_view(['POST'])
def api_records(request):
    serializer = RecordSerializer(data=request.data)
    if serializer.is_valid():
        if serializer.validated_data['rhost'] is None or ipaddress.ip_address(serializer.validated_data['rhost']).is_private:
            country = None
        else:
            country = requests.get(f"https://ipapi.co/{serializer.validated_data['rhost']}/country/").text
        serializer.validated_data['country'] = country
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
