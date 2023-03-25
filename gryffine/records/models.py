from django.db import models
from django_countries.fields import CountryField

from records.notifiers import telegram_notify


class Record(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    hostname = models.CharField(max_length=50)
    service = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    rhost = models.GenericIPAddressField(null=True, blank=True)
    country = CountryField(null=True, blank=True)
    is_successful = models.BooleanField(default=True)
    is_suspicious = models.BooleanField(null=True, blank=True)
    
  def __str__(self):
        message_text = ''
        if self.is_successful:
            message_text += 'Detected successful login '
        else:
            message_text += 'Detected failed login '
        message_text += f'to {self.hostname} with username {self.user} through {self.service}. \n'
        if self.rhost is not None:
            message_text += f'Remote IP: {self.rhost}'
        if self.country.code is not None:
            message_text += f', country of origin {self.country.name}.\n'
        return message_text

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        telegram_notify(str(self))


class Rule(models.Model):
    country = CountryField(null=True, blank=True)
    rhost = models.CharField(max_length=50, null=True, blank=True)


class BlackListRule(Rule):
    pass


class WhitelistRule(Rule):
    pass
