import ipaddress
import requests

from rest_framework import serializers

from records.models import Record


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'timestamp', 'service', 'user',
                  'hostname', 'rhost', 'is_successful')
        model = Record

    def create(self, validated_data):
        if validated_data['rhost'] is None or ipaddress.ip_address(validated_data['rhost']).is_private:
            country = None
        else:
            country = requests.get(f"https://ipapi.co/{validated_data['rhost']}/country/").text
        validated_data['country'] = country
        instance = self.Meta.model.objects.create(**validated_data)
        return instance
