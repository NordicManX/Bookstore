import json

from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from order.factories import UserFactory
from product.factories import CategoryFactory, ProductFactory
from product.models import Product


class TestProductViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        # Criação do usuário e token de autenticação
        self.user = UserFactory()
        token = Token.objects.create(user=self.user)
        token.save()

        # Criação de um produto
        self.product = ProductFactory(
            title="pro controller",
            price=200.00,
        )

    def test_get_all_product(self):
        # Teste para obter todos os produtos
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        response = self.client.get(
            reverse("product-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product_data = json.loads(response.content)

        # Verificando se os dados retornados estão corretos
        self.assertEqual(product_data["results"][0]["title"], self.product.title)
        self.assertEqual(product_data["results"][0]["price"], self.product.price)
        self.assertEqual(product_data["results"][0]["active"], self.product.active)

    def test_create_product(self):
        # Teste para criar um novo produto
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        
        # Criação de uma categoria
        category = CategoryFactory()
        
        # Passando os dados do novo produto, incluindo o ID da categoria
        data = {
            "title": "notebook",
            "price": 800.00,
            "categories": [category.id]  # Corrigido o nome do campo para "categories"
        }

        response = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}),
            data=data,
            format="json"  # Usando format="json" ao invés de content_type
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verificando se o produto foi criado corretamente
        created_product = Product.objects.get(title="notebook")
        self.assertEqual(created_product.title, "notebook")
        self.assertEqual(created_product.price, 800.00)
