from django.contrib import admin

# Register your models here.
from covid_cases.models import Country, DailyReport, State

admin.site.register(Country)
admin.site.register(State)
admin.site.register(DailyReport)
