from bot.bot import Bot
from django.conf import settings
import requests
from main.conf import mailagent_bot_token, mail_contacts
from django.template.loader import render_to_string
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    args = ''
    help = ''
    
    def handle(self, *args, **options):
        pass


# mailagent_bot_token = "001.4217311500.1159573524:1002164570"
# mail_contacts = {
#     "admins": [
#         "efimovsergeipr@mail.ru",
#         ],
#     "channel": [
#         # "@AoLG-JRaQb24KBu3ZwI",
#     ],
# }


# bot = Bot(token=mailagent_bot_token)

# print('hallo welt')
# def send_alert_to_agent(order=None):
    
#     chats_to_send_notifications = mail_contacts['admins']
#     text_to_send = render_to_string('magent.html', {'uuid': order['uuid'],})



addr = 'https://agent.mail.ru/bot/v1/'
method = '​/messages​/sendFile'

url = 'http://127.0.0.1:8000/'
myobj = {'somekey': 'somevalue'}

response = requests.post(url, data = myobj)
print(response.status_code)