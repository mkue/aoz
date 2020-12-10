from django.db import models


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)
    latitude = models.DecimalField(decimal_places=6, max_digits=9, null=True)
    longitude = models.DecimalField(decimal_places=6, max_digits=9, null=True)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    latitude = models.DecimalField(decimal_places=6, max_digits=9, null=True)
    longitude = models.DecimalField(decimal_places=6, max_digits=9, null=True)

    def __str__(self):
        return self.name


class DailyReport(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, related_name="daily_reports")
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, related_name="daily_reports")
    date = models.DateField()
    confirmed = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()

    def __str__(self):
        if self.state:
            return f'{self.country.name} - {self.state.name}'
        else:
            return self.country.name
