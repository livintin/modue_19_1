from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(decimal_places=5, max_digits=20, default=0)
    age = models.IntegerField(default=0)

class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    size = models.DecimalField(decimal_places=4, max_digits=20, default=0)
    description = models.TextField(null=True)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')
