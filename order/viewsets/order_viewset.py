from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from order.models import Order
from order.serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()  
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated] 

    def get_queryset(self):
       
        user = self.request.user
        if user.is_authenticated:
            return Order.objects.filter(user=user)
        return Order.objects.none()
