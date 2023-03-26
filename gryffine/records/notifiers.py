from django.conf import settings
from django.core.mail import send_mail
import requests

from users.models import ExtendedUser


def telegram_notify(message):
    if settings.TELEGRAM_TOKEN:
        ids = _get_tg_ids()
        for tg_id in ids:
            requests.get(f'https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}'
                         f'/sendMessage?chat_id={tg_id}&text={message}')


def email_notify(message):
    if settings.EMAIL_HOST_USER:
        send_mail(
            'New login detected',
            message,
            settings.EMAIL_HOST_USER,
            _get_emails(),
            fail_silently=False,
        )


def _get_tg_ids():
    ids = ExtendedUser.objects.all().values_list('telegram_id', flat=True)
    ids = tuple(filter(None, ids))
    return ids


def _get_emails():
    emails = ExtendedUser.objects.all().values_list('user__email', flat=True)
    emails = tuple(filter(None, emails))
    return emails
