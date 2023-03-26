import django_tables2 as tables

from .models import Record


class LogsTable(tables.Table):
    is_successful = tables.columns.Column(visible=False)
    id = tables.columns.Column(visible=False)
    timestamp = tables.DateTimeColumn(format='Y-m-d H:i:s')

    class Meta:
        model = Record
        row_attrs = {
            "style": lambda record: "background-color: gray" if not record.is_successful
            else "background-color: orange" if record.is_suspicious is None
            else "background-color: #5bff64" if not record.is_suspicious
            else "background-color: #ff5b5b"
        }
        sequence = ('timestamp', 'hostname', 'service',
                    'user', 'rhost', 'country', 'is_suspicious')
        attrs = {"class": "table",
                 "style": "border: 1px solid lightslategray;"}
