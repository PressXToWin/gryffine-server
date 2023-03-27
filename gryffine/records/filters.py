from django_filters import FilterSet

from .models import Record


class RecordFilter(FilterSet):
    class Meta:
        model = Record
        fields = {
            "hostname": ["exact"],
            "service": ["exact"],
            "user": ["contains"],
            "rhost": ["contains"],
            "country": ["exact"],
            "is_successful": ["exact"],
            "is_suspicious": ["exact"],
        }
