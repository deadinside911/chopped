from django.urls import path

from .views import (
    DinerTokenObtainPairView,
)

urlpatterns = [
    path("login/", DinerTokenObtainPairView.as_view(), name="login")
]