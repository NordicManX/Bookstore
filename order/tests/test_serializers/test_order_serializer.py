from django.test import TestCase
from order.factories import OrderFactory
from product.factories import ProductFactory
from order.serializers import OrderSerializer

class TestOrderSerializer(TestCase):
    def setUp(self) -> None:
        # Criando produtos usando o ProductFactory
        self.product_1 = ProductFactory()
        self.product_2 = ProductFactory()

        # Criando a ordem sem a associação direta de produtos
        self.order = OrderFactory()

        # Associando os produtos à ordem usando .set()
        self.order.products.set([self.product_1, self.product_2])
        
        # Inicializando o serializer da ordem
        self.order_serializer = OrderSerializer(self.order)

    def test_order_serializer(self):
        # Testando os dados serializados
        serializer_data = self.order_serializer.data
        self.assertEqual(
            serializer_data["products"][0]["title"], self.product_1.title
        )
        self.assertEqual(
            serializer_data["products"][1]["title"], self.product_2.title
        )
