from records.models import Record, BlackListRule, WhitelistRule
import ipaddress
import requests


def set_country(data):
    if data['rhost'] is None or ipaddress.ip_address(data['rhost']).is_private:
        country = None
    else:
        country = requests.get(f"https://ipapi.co/{data['rhost']}/country/").text
    data['country'] = country


def is_applying(data, ruleset):
    countries = ruleset.values_list('country', flat=True)
    if data['country'] in countries:
        return True


def check_rules(data):
    blacklist = BlackListRule.objects.all()
    whitelist = WhitelistRule.objects.all()
    if is_applying(data, whitelist):
        data['is_suspicious'] = False
    elif is_applying(data, blacklist):
        data['is_suspicious'] = True


def check_record(record):
    set_country(record)
    check_rules(record)