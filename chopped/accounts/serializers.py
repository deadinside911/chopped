from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .token import DinerRefreshToken

class DinerTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        return DinerRefreshToken.for_user(user)

