import ipaddress
import requests

from rest_framework import serializers

from records.models import Record, BlackListRule, WhitelistRule


class RecordSerializer(serializers.ModelSerializer):
    blacklist = BlackListRule.objects.all()
    whitelist = WhitelistRule.objects.all()

    class Meta:
        fields = ('id', 'timestamp', 'service', 'user',
                  'hostname', 'rhost', 'is_successful')
        model = Record

    def is_applying(self, validated_data, ruleset):
        countries = ruleset.values_list('country', flat=True)
        if validated_data['country'] in countries:
            return True

    def create(self, validated_data):
        if validated_data['rhost'] is None or ipaddress.ip_address(validated_data['rhost']).is_private:
            country = None
        else:
            country = requests.get(f"https://ipapi.co/{validated_data['rhost']}/country/").text
        validated_data['country'] = country
        if self.is_applying(validated_data, self.whitelist):
            validated_data['is_suspicious'] = False
        elif self.is_applying(validated_data, self.blacklist):
            validated_data['is_suspicious'] = True
        instance = self.Meta.model.objects.create(**validated_data)
        return instance
