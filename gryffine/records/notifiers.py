from django.conf import settings
import requests

from users.models import ExtendedUser


def telegram_notify(message, key=settings.TELEGRAM_TOKEN):
    if key:
        ids = _get_tg_ids()
        for tg_id in ids:
            requests.get(f'https://api.telegram.org/bot{key}/sendMessage?chat_id={tg_id}&text={message}')


def _get_tg_ids():
    ids = ExtendedUser.objects.all().values_list('telegram_id', flat=True)
    ids = tuple(filter(None, ids))
    return ids
