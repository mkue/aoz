from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name + " - " + self.last_name + " - " + str(self.age)


class Item(models.Model):
    name = models.CharField(max_length=255)
