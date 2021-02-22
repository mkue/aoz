from covid_cases.models import Country
import django


# def getcountry():
#     country_list = Country.objects.all()
#     for country in country_list:
#         print(country.name)
#
#
# getcountry()

from covid_cases.management.controller import out_cases
from covid_cases.models import Country, State, DailyReport

from django.core.management import BaseCommand

class Command(BaseCommand):

   def handle(self, *args, **options):

    out_cases.getcountry()