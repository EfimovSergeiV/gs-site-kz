"""

Scripts

"""

from django.core.management.base import BaseCommand, CommandError
from catalog.models import *


class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        pass


count = 0
queryset = ProductModel.objects.filter()

for prod in queryset:
    queryset.filter(id=prod.id).update(activated=True)