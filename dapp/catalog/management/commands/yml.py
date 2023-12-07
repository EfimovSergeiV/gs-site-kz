""" YML test """

from django.core.management.base import BaseCommand

import json
import requests


class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        pass


# response = requests.get('https://api.webmaster.yandex.net/v4/user', headers={ 'Authorization': '' })

response = requests.get('https://api.webmaster.yandex.net/v4/user/0841001aff5742cfaec72026ef6d4697/hosts')

print(response.text)