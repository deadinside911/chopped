from django.contrib.auth.models import User
from django.db import models


class Diner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateTimeField(null=True)
    