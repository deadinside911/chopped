from rest_framework import serializers

from .models import (
    MenuItem,
    Restaurant,
)

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id", "name"]


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["name", "price", "is_veg", "is_available"]

