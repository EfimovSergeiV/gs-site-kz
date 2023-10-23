from django.core.management.base import BaseCommand, CommandError
from catalog.models import ProductModel
from time import sleep


class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        pass

count = 0
prods_qs = ProductModel.objects.filter(activated=False)

for prod_qs in prods_qs:
    count += 1

    
    print(f'{ count }.\t{prod_qs.name}')
    prod_qs.delete()
