from http.client import HTTPException
from rest_framework import serializers
from .models import Products, Tariff

class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = ('pk', 'name')

class ProductsSerializer(serializers.ModelSerializer):
    tariffs = TariffSerializer(many=True)

    def get_products(self, class_product):
        queryset = Products.objects.filter(class_product__name = class_product)
        serializer = ProductsSerializer(queryset, many=True)
        return serializer

    class Meta:
        model = Products
        fields = ('pk', 'name', 'tariffs')


class PrductsPriceSerializer(serializers.Serializer):

    def create(self, data):
        print(data)
        products = {}
        data = data['request']
        for key in data.keys():
            if not key.isdigit():
                raise HTTPException(400, 'key must be integer')
            if not isinstance(data[key], int):
                raise HTTPException(400, 'value must be integer')
            
            try:
                product = Products.objects.get(pk=int(key))
            except Products.DoesNotExist:
                raise HTTPException(404, f"product with id {key} does not exist")
            if products.get(data[key]) is None:
                products[data[key]] = [{'pk': key, 'custom_price': product.custom_price}]
            else:
                products[data[key]].append({'pk': key, 'custom_price': product.custom_price})
        
        
        return_data = {}
        for data in products.keys():
            price = 0
            discount_price = 0
            try:
                tariff = Tariff.objects.get(pk=int(data))
            except Tariff.DoesNotExist:
                raise HTTPException(404, f"tariff with id {data} does not found")
            discount_product_price = tariff.products_price.get(str(len(products[data])) if len(products[data]) <= 3 else '3')
            product_price = tariff.products_price.get('1')
            for product in products[data]:
                if product['custom_price'] is None:
                    price += product_price
                    discount_price += discount_product_price
                else:
                    price += product['custom_price']
                    discount_price += product['custom_price']
            if price != discount_price:
                return_data[tariff.name] = {'price': price, 'discount_price': discount_price}
            else:
                return_data[tariff.name] = {'price': price}
        return return_data
