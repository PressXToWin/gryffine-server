from rest_framework import viewsets, mixins
from records.models import Record
from .serializers import RecordSerializer


class RecordViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
