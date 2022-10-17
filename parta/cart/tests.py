from http import HTTPStatus
import json

from django.core.management import call_command
from rest_framework.test import APITestCase
from django.urls import reverse

from .models import Products

class TestProducts(APITestCase):
    """ Test products endpoints """

    def setUp(self) -> None:
        call_command('loaddata', 'db.json', verbosity=0)

    def test_products_list(self) -> None:
        api_path = reverse('products')
        products = Products.objects.all()
        response = self.client.get(api_path, {'class_product': 9})
        self.assertEqual(len(products), len(response.data))

    def test_products_price(self) -> None:
        api_path = reverse('products_price')
        response = self.client.post(api_path, json.dumps({'1': 1, '2': 1}), content_type='application/json')
        self.assertEqual(response.status_code, HTTPStatus.OK)
