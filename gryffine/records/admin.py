from django.contrib import admin
from .models import WhitelistRule, BlackListRule

admin.site.register(WhitelistRule)
admin.site.register(BlackListRule)
