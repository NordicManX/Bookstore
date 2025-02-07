import json
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from product.factories import CategoryFactory, ProductFactory
from order.factories import UserFactory
from product.models import Product


class TestProductViewSet(APITestCase):
    client = APIClient()
    def setUp(self):
        self.user = UserFactory()
        self.product = ProductFactory(title="pro-controller", price=100.00)

    def test_get_product_list(self):
        response = self.client.get(reverse("product-list", kwargs={"version": "v1"}))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product_data = json.loads(response.content)[0]  
        
        self.assertEqual(product_data["title"], self.product.title)
        self.assertEqual(product_data["price"], self.product.price)
        self.assertEqual(product_data["active"], self.product.active)

    def test_create_product(self):
        category = CategoryFactory()
        data = {
            "title": "notebook",
            "price": 800.00,
            "categories_id": [category.id], 
        }
        
        response = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}),
            data=json.dumps(data),
            content_type="application/json",
        )
        print(response.content)  # Pode remover após depuração
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        created_product = Product.objects.get(title="notebook")
        self.assertEqual(created_product.title, "notebook")
        self.assertEqual(created_product.price, 800.00)
          
        