from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()

    objects = models.Manager()

    def __lt__(self, other):
        return self.age < other.age

    def __str__(self):
        return self.first_name + " - " + self.last_name + " - " + str(self.age)


class Item(models.Model):
    name = models.CharField(max_length=255)


class Entry(models.Model):
    blog = models.ForeignKey(Customer, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline
