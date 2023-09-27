"""

price to tenge

"""

from django.core.management.base import BaseCommand, CommandError
from catalog.models import *


class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        pass


PROCENT = 10

count = 0
queryset = ProductModel.objects.filter(activated=True)

for prod_qs in queryset:
    count += 1
    new_price = int(prod_qs.price) * 5

    price = new_price

    while price % 10 != 0:
        price += 1

    print(f'{count}. { prod_qs.id }: { prod_qs.price } > { price } { prod_qs.name }')

    queryset.filter(id=prod_qs.id).update(price = price, currency = 'KZT')