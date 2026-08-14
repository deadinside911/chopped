from rest_framework import status
from rest_framework import generics
from rest_framework.views import (
    APIView,
    Response
)

from firestore.client import get_db

from .serializers import (
    RestaurantSerializer,
)


class GetAllRestaurantsView(generics.ListAPIView):
    serializer_class = RestaurantSerializer


class TestAPIView(APIView):
    def get(self, request):
        firestore_db = get_db()
        firestore_db.collection("tables").document("table_1").set({"example": "value"})

        return Response("check", status=status.HTTP_200_OK)

class GetRestaurantMenuView():
    pass


class CreateTableView():
    pass


class JoinTableView():
    pass

