from django.urls import path

from .views import (
    GetAllVendorsView,
)

urlpatterns = [
    path("get-all-vendors/", GetAllVendorsView.as_view(), name="get-all-vendors"),
]