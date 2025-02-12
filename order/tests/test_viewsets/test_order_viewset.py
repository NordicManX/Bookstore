import json
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import reverse
from product.factories import CategoryFactory, ProductFactory
from order.factories import OrderFactory, UserFactory
from order.models import Order

class TestViewSet(APITestCase):  # Corrigido para herdar de APITestCase
    
    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()
        token = Token.objects.create(user=self.user)
        
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")  # Configura o token para todos os testes
        
        self.category = CategoryFactory(title='technology')
        self.product = ProductFactory(title='mouse', price=100)
        self.product.category.add(self.category)  # Relacionamento ManyToMany ajustado
        
        self.order = OrderFactory()
        self.order.product.add(self.product)  # Adiciona o produto ao pedido

    def test_order(self):
        response = self.client.get(reverse('order-list', kwargs={'version': 'v1'}))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        order_data = json.loads(response.content)[0]
        
        self.assertEqual(order_data['result'][0]['product'][0]['title'], self.product.title)
        self.assertEqual(order_data['result'][0]['product'][0]['price'], self.product.price)
        self.assertEqual(order_data['result'][0]['product'][0]['active'], self.product.active)
        self.assertEqual(order_data['result'][0]['product'][0]['category'][0]['title'], self.category.title)

    def test_create_order(self):  # Corrigida a indentação
        user = UserFactory()
        product = ProductFactory()
        
        data = {
            'product': [product.id],
            'user': user.id
        }
        
        response = self.client.post(
            reverse('order-list', kwargs={'version': 'v1'}),
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_order = Order.objects.get(user=user)
        self.assertIsNotNone(created_order)  # Verifica se o pedido foi criado
