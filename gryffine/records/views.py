from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django_tables2.config import RequestConfig
from django_tables2.export.export import TableExport

from .models import Record
from .tables import LogsTable


@login_required
def index(request):
    order_by = request.GET.get("sort", '-id')
    per_page_options = (25, 50, 100, 200)
    per_page = request.GET.get("per_page", 25)
    table = LogsTable(Record.objects.all().order_by(order_by))
    table.paginate(page=request.GET.get("page", 1), per_page=per_page)
    RequestConfig(request).configure(table)
    export_formats = ("csv", "xls")
    export_format = request.GET.get("_export", None)
    table.visible = ('timestamp', 'service', 'user', 'rhost', 'country')
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response("table.{}".format(export_format))

    context = {
        'title': 'Authentication logs',
        "table": table,
        'export_formats': export_formats,
        'per_page_options': per_page_options
    }

    return render(request, 'records/index.html', context)
