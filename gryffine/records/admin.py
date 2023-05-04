from django.contrib import admin

from .models import BlackListRule, WhitelistRule

admin.site.register(WhitelistRule)
admin.site.register(BlackListRule)
