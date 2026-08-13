from django.urls import path

from .views import (
    GetAllRestaurantsView,
)

urlpatterns = [
    path("get-all-vendors/", GetAllRestaurantsView.as_view(), name="get-all-vendors"),
]