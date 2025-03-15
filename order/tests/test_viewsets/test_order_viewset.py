import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from order.factories import OrderFactory, UserFactory
from order.models import Order
from product.factories import CategoryFactory, ProductFactory
from product.models import Product


class TestOrderViewSet(APITestCase):

    client = APIClient()

    def setUp(self):
        # Criando uma categoria e um produto para o pedido
        self.category = CategoryFactory(title="technology")
        self.product = ProductFactory(
            title="mouse", price=100, category=[self.category]
        )
        # Criando um pedido com um produto
        self.order = OrderFactory(products=[self.product])

    def test_order(self):
        # Testando o endpoint GET para obter todos os pedidos
        response = self.client.get(
            reverse("order-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificando os dados retornados
        order_data = json.loads(response.content)
        self.assertEqual(
            order_data["results"][0]["products"][0]["title"], self.product.title
        )
        self.assertEqual(
            order_data["results"][0]["products"][0]["price"], self.product.price
        )
        self.assertEqual(
            order_data["results"][0]["products"][0]["active"], self.product.active
        )
        self.assertEqual(
            order_data["results"][0]["products"][0]["category"][0]["title"],
            self.category.title,
        )

    def test_create_order(self):
        # Criando um usuário e um produto
        user = UserFactory()
        product = ProductFactory()
        
        # Passando os dados para criar um pedido
        data = {
            "products": [product.id],  # Usando "products" ao invés de "products_id"
            "user": user.id
        }

        response = self.client.post(
            reverse("order-list", kwargs={"version": "v1"}),
            data=data,
            format="json",  # Usando format="json" ao invés de content_type
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verificando se o pedido foi criado
        created_order = Order.objects.get(user=user)
        self.assertTrue(created_order.products.filter(id=product.id).exists())
        self.assertEqual(created_order.user, user)
