from rest_framework import generics

from .serializers import (
    RestaurantSerializer,
)


class GetAllRestaurantsView(generics.ListAPIView):
    serializer_class = RestaurantSerializer


class GetRestaurantMenuView():
    pass


class CreateTableView():
    pass


class JoinTableView():
    pass

