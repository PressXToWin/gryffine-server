import django_tables2 as tables

from .models import Record


class LogsTable(tables.Table):
    is_successful = tables.columns.Column(visible=False)
    timestamp = tables.DateTimeColumn(format='Y-m-d H:i:s')

    class Meta:
        model = Record
        exclude = ('id', )
        row_attrs = {
            "style": lambda record: "background-color: #5bff64" if record.is_successful else "background-color: #ff5b5b"
        }
        sequence = ('timestamp', 'hostname', 'service', 'user', 'rhost', 'country')
        attrs = {"class": "table",
                 "style": "border: 1px solid lightslategray;"}
