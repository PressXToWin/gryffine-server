import ipaddress

import requests
from django.conf import settings

from records.models import BlackListRule, WhitelistRule


def set_country(data):
    if data['rhost'] is None or ipaddress.ip_address(data['rhost']).is_private:
        country = None
    else:
        country = requests.get(
            f"https://ipapi.co/{data['rhost']}/country/"
        ).text
    data['country'] = country


def is_applying(data, ruleset):
    countries = [country
                 for country in ruleset.values_list('country', flat=True)
                 if country is not None]
    if data['country'] in countries:
        return True
    ip_subnets = [ipaddress.ip_network(ip)
                  for ip in ruleset.values_list('rhost', flat=True)
                  if ip is not None]
    for subnet in ip_subnets:
        if data['rhost'] is not None and ipaddress.ip_address(
                data['rhost']) in subnet:
            return True


def check_rules(data):
    blacklist = BlackListRule.objects.all()
    whitelist = WhitelistRule.objects.all()
    if settings.CONSIDER_LOCAL_WHITELISTED and (
            not data['rhost']
            or ipaddress.ip_address(data['rhost']).is_private):
        data['is_suspicious'] = False
    elif is_applying(data, whitelist):
        data['is_suspicious'] = False
    elif is_applying(data, blacklist):
        data['is_suspicious'] = True


def check_record(record):
    set_country(record)
    check_rules(record)
