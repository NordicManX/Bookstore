from django.test import TestCase

from product.factories import CategoryFactory, ProductFactory
from product.serializers import ProductSerializer


class TestProductSerializer(TestCase):
    def setUp(self) -> None:
        # Criando a categoria
        self.category = CategoryFactory(title="technology")

        # Criando o produto
        self.product_1 = ProductFactory(title="mouse", price=100)

        # Associando a categoria ao produto
        self.product_1.category.set([self.category])

        # Inicializando o serializer do produto
        self.product_serializer = ProductSerializer(self.product_1)

    def test_product_serializer(self):
        # Testando os dados serializados
        serializer_data = self.product_serializer.data
        self.assertEqual(serializer_data["price"], 100)
        self.assertEqual(serializer_data["title"], "mouse")
        self.assertEqual(
            serializer_data["category"][0]["title"], "technology"
        )
