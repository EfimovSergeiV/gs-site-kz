from opensearchpy import OpenSearch

from django.core.management.base import BaseCommand
from catalog.models import ProductModel
from main.conf import OPENSEARCH_DSL

class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        pass

auth = OPENSEARCH_DSL['default']

# Конфигурация подключения к OpenSearch
opensearch_client = OpenSearch(
    hosts=[{'host': 'search.glsvar.ru', 'port': 443}],
    http_auth=auth['http_auth'],
    use_ssl=True,
    verify_certs=True
)

index_name = 'productskz'

# Функция для записи данных в индекс
def index_document(index_name, doc_id, document):
    response = opensearch_client.index(
        index=index_name,
        id=doc_id,
        body=document,
        refresh=True 
    )
    return response


for product in ProductModel.objects.filter(activated=True):
    document = {
        'id': product.id,
        'vcode': product.vcode,
        'name': product.name,
        'keywords': product.keywords,
    }
    response = index_document(index_name, doc_id=product.id, document=document)
    print(f'Document indexed: {response}')