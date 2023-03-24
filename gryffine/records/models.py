from django.db import models
from django_countries.fields import CountryField


class Record(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    hostname = models.CharField(max_length=50)
    service = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    rhost = models.GenericIPAddressField(null=True, blank=True)
    country = CountryField(null=True, blank=True)
    is_successful = models.BooleanField(default=True)
    is_suspicious = models.BooleanField(null=True, blank=True)


class Rule(models.Model):
    country = CountryField(null=True, blank=True)
    rhost = models.CharField(max_length=50, null=True, blank=True)


class BlackListRule(Rule):
    pass


class WhitelistRule(Rule):
    pass
