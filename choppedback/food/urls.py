from django.urls import path

from .views import (
    GetAllRestaurantsView,
    TestAPIView,
)

urlpatterns = [
    path("get-all-vendors/", GetAllRestaurantsView.as_view(), name="get-all-vendors"),
    path("test", TestAPIView.as_view(), name="test-view"),
]