"""

"""
from django.core.management.base import BaseCommand
from pathlib import Path
from time import sleep
import json

from catalog.models import ProductModel


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


class Command(BaseCommand):
    args = ''
    help = ''

    queryset = ProductModel.objects.all()

    def handle(self, *args, **options):

        with open(f"{ BASE_DIR }/files/output.json", 'r') as file:
            data = json.load(file)
            counter = 0

            for product in data:
                counter += 1

                product_qs = self.queryset.filter(id = product["id"])
                
                writed_data = {}
                if  product["vcode"]:
                    writed_data["vcode"] = str(product["vcode"])

                if product["name"]:
                    writed_data["name"] = product["name"]

                if product["price"]:
                    writed_data["price"] = product["price"]

                if product["dissable"]:
                    writed_data["activated"] = False

                print(f'\n{counter}.\t{product}\n{writed_data}')
                product_qs.update(**writed_data)

                








