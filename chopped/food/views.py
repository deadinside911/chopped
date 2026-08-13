from rest_framework import generics

from .serializers import (
    RestaurantSerializer,
)


class GetAllVendorsView(generics.ListAPIView):
    serializer_class = RestaurantSerializer

