from django.db import models


class Table(models.Model):
    join_code = models.CharField(max_length=6)


class Restaurant(models.Model):
    name = models.CharField()


class MenuItem(models.Model):
    name = models.CharField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    price = models.DecimalField()
    is_veg = models.BooleanField()
    is_available = models.BooleanField()
