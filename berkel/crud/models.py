from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    age = models.IntegerField()


class Item(models.Model):
    name = models.CharField(max_length=255)