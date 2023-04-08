from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
import requests

User = get_user_model()


def send_notify(record):
    if record.is_successful or settings.NOTIFY_NOT_SUCCESSFUL:
        if record.is_suspicious or (
                record.is_suspicious is None and settings.NOTIFY_UNKNOWN_SUSPICIOUS) or (
                record.is_suspicious is False and settings.NOTIFY_NOT_SUSPICIOUS):
            telegram_notify(str(record))
            email_notify(str(record))


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
    ids = User.objects.all().values_list('telegram_id', flat=True)
    ids = tuple(filter(None, ids))
    return ids


def _get_emails():
    emails = User.objects.all().values_list('user__email', flat=True)
    emails = tuple(filter(None, emails))
    return emails
