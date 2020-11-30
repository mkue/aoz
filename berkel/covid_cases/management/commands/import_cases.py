import requests
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Import new Covid-19 cases"

    def add_arguments(self, parser):
        parser.add_argument("date", nargs="?", default="03-22-2020")

    def handle(self, *args, **options):
        r = requests.get(
            f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/"
            f"csse_covid_19_daily_reports/{options['date']}.csv")
        print(r.status_code)