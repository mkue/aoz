from django.db import models


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(decimal_places=6, max_digits=9)
    longitude = models.DecimalField(decimal_places=6, max_digits=9)


class State(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    latitude = models.DecimalField(decimal_places=6, max_digits=9)
    longitude = models.DecimalField(decimal_places=6, max_digits=9)


class DailyReport(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, related_name="daily_reports")
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, related_name="daily_reports")
    date = models.DateField()
    confirmed = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()
    update = models.DateTimeField()
