from django.contrib import admin

from .models import (
    MenuItem,
    Restaurant,
    Table,
)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "is_veg", "is_available"]


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ["join_code"]
