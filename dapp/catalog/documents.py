from catalog.models import ProductModel
from django_opensearch_dsl import Document
from django_opensearch_dsl.registries import registry
from django_opensearch_dsl.fields import GeoPointField


@registry.register_document
class ProductDocument(Document):
    """ Elastic """

    class Index:
        name = 'productskz'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = ProductModel
        fields = [
            'id',
            'vcode',
            'name',
            'keywords',
        ]
