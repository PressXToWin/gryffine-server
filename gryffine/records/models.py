from django.db import models
from django_countries.fields import CountryField
from users.models import ExtendedUser


import os
import requests
from dotenv import load_dotenv
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver


load_dotenv()

TELEGRAM_KEY = os.getenv('TELEGRAM_TOKEN')
EMAIL_USERNAME = os.getenv('EMAIL_USERNAME')
EMAIL_PASSWORD = os.getenv('EMAIL_USERNAME')
SUBJECT = 'New login detected'


class Record(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    hostname = models.CharField(max_length=50)
    service = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    rhost = models.GenericIPAddressField(null=True, blank=True)
    country = CountryField(null=True, blank=True)
    is_successful = models.BooleanField(default=True)

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


def telegram_notify(tg_ids: tuple, message, key=TELEGRAM_KEY):
    for tg_id in tg_ids:
        requests.get(f'https://api.telegram.org/bot{key}/sendMessage?chat_id={tg_id}&text={message}')

# Here will be email notify.
    # send_mail(message=message, recipient_list=recipient_list, subject=subject, auth_user=auth_user, auth_password=auth_password)


@receiver(post_save, sender=Record)
def notify(sender, instance, raw, using, update_fields, **kwargs):
    message = str(instance)
    ids = ExtendedUser.objects.all().values_list('telegram_id', flat=True)
    telegram_notify(ids, message=message)
