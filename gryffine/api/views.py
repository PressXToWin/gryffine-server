from rest_framework import mixins, viewsets

from records.models import Record

from .serializers import RecordSerializer


class RecordViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
