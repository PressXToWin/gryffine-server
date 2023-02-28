from rest_framework import serializers

from records.models import Record


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'timestamp', 'service', 'user',
                  'hostname', 'rhost', 'is_successful')
        model = Record
