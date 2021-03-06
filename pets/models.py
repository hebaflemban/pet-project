from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    available = models.BooleanField(default = True)
    image = models.ImageField()
    price = models.DecimalField()
