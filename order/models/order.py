from django.db import models
from django.contrib.auth.models import User
from product.models.product import Product

class Order(models.Model):
    product = models.ManyToManyField(Product, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']  # Ordenar por ID decrescente para mostrar os pedidos mais recentes primeiro
