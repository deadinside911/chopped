from django.contrib import admin

from .models import Diner

@admin.register(Diner)
class DinerAdmin(admin.ModelAdmin):
    list_display = ["user__first_name", "birthday"]
