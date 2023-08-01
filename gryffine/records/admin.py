from django.contrib import admin

from .models import BlackListRule, WhiteListRule

admin.site.register(WhiteListRule)
admin.site.register(BlackListRule)
