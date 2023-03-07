from records.models import Record
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_KEY = os.getenv('TELEGRAM_KEY')
EMAIL_USERNAME = os.getenv('EMAIL_USERNAME')
EMAIL_PASSWORD = os.getenv('EMAIL_USERNAME')


def textmaker(record: Record):
    message_text = ''
    if record.is_successful:
        message_text += 'Detected successful login '
    else:
        message_text += 'Detected failed login '
    message_text += f'to {record.hostname} with username {record.user} through {record.service}. \n '
    if record.rhost is not None:
        message_text += f'Remote IP: {record.rhost}'
    if record.country is not None:
        message_text += f', country of origin {record.country.verbose_name}'
    message_text += '.\n'
    return message_text

