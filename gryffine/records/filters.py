from django_filters import FilterSet

from .models import Record


class RecordFilter(FilterSet):
    class Meta:
        model = Record
        fields = {"service": ["exact", "contains"], "user": ["exact"]}
