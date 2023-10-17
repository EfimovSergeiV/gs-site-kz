from django.core.management.base import BaseCommand, CommandError
from pathlib import Path
from bot.bot import Bot
from main.conf import mailagent_bot_token

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        pass


target = "@AoLIhsdsR3MfM6vQHhg"

bot = Bot(token=mailagent_bot_token)

def image_cb():
    bot.send_file(
        chat_id= target,
        file = open('./image.jpg', 'rb')
    )
image_cb()