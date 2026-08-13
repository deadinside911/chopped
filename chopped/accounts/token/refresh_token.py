from rest_framework_simplejwt.tokens import RefreshToken


class DinerRefreshToken(RefreshToken):
    @classmethod
    def for_user(cls, user):
        return super().for_user(user)

