import csv
import logging
from datetime import date

from covid_cases.models import Country, DailyReport, State


def import_csv_file(file_content: str, execution_date: date):
    reader = csv.reader(file_content.splitlines()[1:], delimiter=",")
    for entries in reader:
        try:
            country = Country.objects.get(name=entries[3])
        except Country.DoesNotExist:
            country = Country(
                name=entries[3],
                latitude=entries[5] if entries[5] else None,
                longitude=entries[6] if entries[6] else None,
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
                    longitude=entries[6] if entries[6] else None,
                )
                state.save()
        else:
            state = None

        try:
            daily_report = DailyReport.objects.get(country=country, state=state, date=execution_date)
            logging.debug(f"Daily report for {country} already exists")
            daily_report.confirmed = int(entries[7])
            daily_report.deaths = int(entries[8])
            daily_report.recovered = int(entries[9])
        except DailyReport.DoesNotExist:
            daily_report = DailyReport(
                country=country,
                state=state,
                date=execution_date,
                confirmed=int(entries[7]),
                deaths=int(entries[8]),
                recovered=int(entries[9]),
            )
        daily_report.save()
