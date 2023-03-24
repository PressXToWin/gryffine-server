from rest_framework import serializers
from .services import check_record
from records.models import Record, BlackListRule, WhitelistRule


class RecordSerializer(serializers.ModelSerializer):
    blacklist = BlackListRule.objects.all()
    whitelist = WhitelistRule.objects.all()

    class Meta:
        fields = ('id', 'timestamp', 'service', 'user',
                  'hostname', 'rhost', 'is_successful')
        model = Record

    def create(self, validated_data):
        check_record(validated_data)
        instance = self.Meta.model.objects.create(**validated_data)
        return instance
