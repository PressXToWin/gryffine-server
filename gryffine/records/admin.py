from django.contrib import admin
from .models import Record, WhitelistRule, BlackListRule

# admin.site.register(Record)
admin.site.register(WhitelistRule)
admin.site.register(BlackListRule)