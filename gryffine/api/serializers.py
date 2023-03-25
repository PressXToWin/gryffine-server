from rest_framework import serializers
from .services import check_record
from records.models import Record


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'timestamp', 'service', 'user',
                  'hostname', 'rhost', 'is_successful')
        model = Record

    def create(self, validated_data):
        check_record(validated_data)
        instance = self.Meta.model.objects.create(**validated_data)
        return instance
