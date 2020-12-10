import csv
from datetime import datetime

import requests
from django.db.transaction import atomic

from covid_cases.models import Country, State, DailyReport
from django.core.management import BaseCommand


def get_date_from_entry(entry: str):
    try:
        return datetime.strptime(entry, '%Y-%m-%d %H:%M:%S').date()
    except ValueError:
        return datetime.strptime(entry, '%m/%d/%y %H:%M').date()


class Command(BaseCommand):
    help = "Import new Covid-19 cases"

    def add_arguments(self, parser):
        parser.add_argument("date", nargs="?", default="03-24-2020")

    @atomic
    def handle(self, *args, **options):
        r = requests.get(f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/"
                         f"csse_covid_19_daily_reports/{options['date']}.csv")
        reader = csv.reader(r.text.splitlines()[1:], delimiter=',')
        for entries in reader:
            try:
                country = Country.objects.get(name=entries[3])
            except Country.DoesNotExist:
                country = Country(
                    name=entries[3],
                    latitude=entries[5],
                    longitude=entries[6]
                )
                country.save()

            if entries[2]:
                try:
                    state = State.objects.get(name=entries[2], country=country)
                except State.DoesNotExist:
                    state = State(
                        name=entries[2],
                        country=country,
                        latitude=entries[5] if entries[5] else None,
                        longitude=entries[6] if entries[6] else None
                    )
                    state.save()
            else:
                state = None
            daily_report = DailyReport(
                country=country,
                state=state,
                date=get_date_from_entry(entries[4]),
                confirmed=int(entries[7]),
                deaths=int(entries[8]),
                recovered=int(entries[9])
            )
            daily_report.save()
