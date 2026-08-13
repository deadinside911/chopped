from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import DinerTokenObtainPairSerializer


class DinerTokenObtainPairView(TokenObtainPairView):
    serializer_class = DinerTokenObtainPairSerializer
