from django.db import models


class Table(models.Model):
    join_code = models.CharField(max_length=6)


class Restaurant(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    # stored in smallest possible currency (INR 0.01)
    price = models.IntegerField()

    is_veg = models.BooleanField()
    is_available = models.BooleanField()
