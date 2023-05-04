from rest_framework import serializers

from records.models import Record

from .services import check_record


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = ('id', 'timestamp', 'service', 'user',
                  'hostname', 'rhost', 'is_successful')

    def create(self, validated_data):
        check_record(validated_data)
        instance = self.Meta.model.objects.create(**validated_data)
        return instance
