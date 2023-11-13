from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from catalog.models import *


class CategoryRecursiveSerializer(serializers.ModelSerializer):
    """MPTT категории с потомками"""
    name = serializers.CharField()
    inserted = serializers.ListField(child=RecursiveField(), source='get_children')

    class Meta:
        model = CategoryModel
        fields = ('id','name', 'icon', 'level', 'inserted', 'related')


""" СЕРИАЛИЗАЦИЯ ДОПОЛНИТЕЛЬНЫХ ПОЛЕЙ ПРОДУКТА """

class PriceSerializer(serializers.ModelSerializer):
    """Сериализация цен на товар"""

    class Meta:
        model = PriceModel
        fields = ('shop', 'price', 'currency', 'quantity', 'status',)

class AvailableSerializer(serializers.ModelSerializer):
    """ Наличие товара по магазинам """
    class Meta:
        model = AvailableModel
        fields = ('shop', 'status', 'quantity',)

class BrandProductSerializer(serializers.ModelSerializer):
    """Сериализация брендов"""
    class Meta:
        model = BrandProductModel
        fields = ('id', 'brand', 'image', 'carousel', 'description')

class PropOpsSerializer(serializers.ModelSerializer):
    """ Значения свойств товаров, для подсказки по фильтрам. """

    class Meta:
        model = PropOpsModel
        fields = ('id', 'name', 'ops', 'opskey',)

class PropsNameSerializer(serializers.ModelSerializer):
    prop_ops = PropOpsSerializer(many=True)

    """ Названия свойств товара для фильтров"""
    class Meta:
        model = PropsNameModel
        fields = (
            'id', 
            'name', 
            'description', 
            'propwidget', 
            'prop_alias', 
            'prop_ops',
            )

class PropStrSerializer(serializers.ModelSerializer):
    """Строковые свойства товара"""
    class Meta:
        model = PropStrModel
        fields = ('id', 'name', 'qname', 'value')

class ProductImageSerializer(serializers.ModelSerializer):
    """Изображение продукта"""

    class Meta:
        model = ProductImageModel
        fields = ('id', 'image')
     

class BreadCrumbSerializer(serializers.ModelSerializer):
    """Название категории"""

    class Meta:
        model = CategoryModel
        fields = (
            'id', 
            'name', 
            'parent'
            )


class CategorySerializer(serializers.ModelSerializer):
    """Название категории"""

    class Meta:
        model = CategoryModel
        fields = ('id', 'name', 'parent', )


class ProductSetSerializer(serializers.ModelSerializer):
    """Дополнительные комплекты товаров"""

    class Meta:
        model = ProductSetModel
        fields = ('id', 'vcode', 'name', 'price', 'preview_image', 'description',)

class ProductCompSerializer(serializers.ModelSerializer):
    """Составные части товаров"""

    class Meta:
        model = ProductCompModel
        fields = ('id', 'rel_id', 'completed' )

class DocumentSerializer(serializers.ModelSerializer):
    """ Дополнительные комплекты товаров"""

    class Meta:
        model = DocumentModel
        fields = ('id', 'name', 'description', 'doc',)


class ExternalLinkSerializer(serializers.ModelSerializer):
    """Дополнительные комплекты товаров"""

    class Meta:
        model = ExternalLinkModel
        fields = ('id', 'name', 'description',  'url',)

# class CatalogFileSerializer(serializers.ModelSerializer):
#     """Файлы какталога (!)"""

#     class Meta:
#         model = CatalogFileModel
#         fields = ('id', 'name', 'description', 'file',)


"""Сериализация продуктов """
class ListProductsSerializer(serializers.ModelSerializer):
    """Список продуктов"""
    # prod_price = PriceSerializer(many=True)
    # prod_available = AvailableSerializer(many=True)
    product_comp = ProductCompSerializer(many=True)
    brand = BrandProductSerializer()
    propstrmodel = PropStrSerializer(many=True)
    
    class Meta:
        model = ProductModel
        fields = (
            'id',
            'vcode',
            'name',
            'description',
            'promo',
            'discount',
            'rating',  
            'preview_image',
            # 'prod_price',
            # 'price_status',
            'price',
            'currency',
            'status',
            'product_comp',
            'brand',
            'propstrmodel', 
            )

from django.utils.html import strip_tags
class ProductSerializer(serializers.ModelSerializer):
    """Выбранный продукт"""
    # prod_price = PriceSerializer(many=True)
    # prod_available = AvailableSerializer(many=True)
    propstrmodel = PropStrSerializer(many=True)
    category = CategorySerializer()
    brand = BrandProductSerializer()
    product_set = ProductSetSerializer(many=True)
    product_comp = ProductCompSerializer(many=True)
    prod_img = ProductImageSerializer(many=True)
    prod_doc = DocumentSerializer(many=True)
    prod_link = ExternalLinkSerializer(many=True)

    clean_desc = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        fields = (
            'id', 
            'vcode',
            'name', 
            'description',
            'clean_desc',
            'preview_image', 
            'rating',
            'promo',
            'discount',
            'related',
            'keywords',
            'price',
            'currency',
            'status',
            'propstrmodel', 
            'category', 
            'brand', 
            'product_set',
            'product_comp',
            'prod_img',
            'prod_doc',
            'prod_link'
            )
        
    def get_clean_desc(self, instance):
        # Возвращает описание без тегов, для СЕО
        data = strip_tags(instance.description.replace('\r', '').replace('\n', '').replace('&laquo', '').replace('&raquo', ''))
        if len(data) > 160:
            data = f'{data[0: 160]}...'
        return data



"""Интеграции с сервисами"""

class ProdSerializer(serializers.ModelSerializer):
    """Сериализатор продукта for 1C"""
    class Meta:
        model = ProductModel
        fields = ['id', 'vcode',]


class OneSPriceSerializer(serializers.ModelSerializer):
    """Сериализация цен на товар для 1С"""

    class Meta:
        model = PriceModel
        fields = ('id', 'price', 'shop', 'currency')


""" СЕРИАЛИЗАТОРЫ ПРОЧИХ ПРЕДСТАВЛЕНИЙ КАТАЛОГА """

class RecommendSerializer(serializers.ModelSerializer):
    """ Рекомендованные товары"""
    propstrmodel = PropStrSerializer(many=True)

    class Meta:
        model = ProductModel
        fields = ('id', 'vcode', 'description' ,'name', 'rating', 'preview_image', 'price', 'currency', 'propstrmodel')


# class GetZIPCitySerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = CityModel
#         fields = ('zip',)

class ShopAdrSerializer(serializers.ModelSerializer):
    """ """
#    zip = GetZIPCitySerializer()

    class Meta:
        """
        Служит для идентификации магазина по городу
        Несёт информацию для header на фронте
        """
        model = ShopAdressModel
        fields = ('id', 'zip', 'phone', 'adress',)


class CitySerializer(serializers.ModelSerializer):
    """ """
    class Meta:
        """
        Служит для идентификации магазина по городу
        Несёт информацию для header на фронте
        """
        model = CityModel
        fields = ('id', 'zip', 'city', 'phone', 'phone_link',)


class ShopAdressSerializer(serializers.ModelSerializer):
    """ Адреса магазинов """

    class Meta:
        model = ShopAdressModel
        fields = '__all__'


# Поиск по сайту
class ProductKeywordSerializer(serializers.ModelSerializer):
    """ Сериализатор ключевых слов продукта """

    class Meta:
        model = ProductKeywordModel
        fields = '__all__'


class SearchSerializer(serializers.ModelSerializer):
    """ Поиск по каталогу товаров """
    # keyword = ProductKeywordSerializer(many=True)

    class Meta:
        model = ProductModel
        fields = (
            'id', 
            'name',
            'price',
            'preview_image',
            )