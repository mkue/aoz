import csv
import logging
from datetime import date
from enum import Enum
from typing import List

from covid_cases.models import Country, DailyReport, State


class Columns(Enum):
    STATE = 2
    COUNTRY = 3
    LATITUDE = 5
    LONGITUDE = 6
    CONFIRMED = 7
    DEATHS = 8
    RECOVERED = 9


def get_value(row: List[str], column: Columns, convert_fct=lambda x: x if x else None):
    val = row[column.value]
    try:
        return convert_fct(val)
    except (TypeError, ValueError):
        return 0


def import_csv_file(file_content: str, execution_date: date):
    reader = csv.reader(file_content.splitlines()[1:], delimiter=",")
    for entries in reader:
        country_name = get_value(entries, Columns.COUNTRY)
        try:
            country = Country.objects.get(name=country_name)
        except Country.DoesNotExist:
            country = Country(
                name=country_name,
                latitude=get_value(entries, Columns.LATITUDE, convert_fct=float),
                longitude=get_value(entries, Columns.LONGITUDE, convert_fct=float),
            )
            country.save()

        state_name = get_value(entries, Columns.STATE)
        if state_name:
            try:
                state = State.objects.get(name=state_name, country=country)
            except State.DoesNotExist:
                state = State(
                    name=state_name,
                    country=country,
                    latitude=get_value(entries, Columns.LATITUDE, convert_fct=float),
                    longitude=get_value(entries, Columns.LONGITUDE, convert_fct=float),
                )
                state.save()
        else:
            state = None

        try:
            daily_report = DailyReport.objects.get(country=country, state=state, date=execution_date)
            logging.debug(f"Daily report for {country} already exists")
            daily_report.confirmed = get_value(entries, Columns.CONFIRMED, convert_fct=int)
            daily_report.deaths = get_value(entries, Columns.DEATHS, convert_fct=int)
            daily_report.recovered = get_value(entries, Columns.RECOVERED, convert_fct=int)
        except DailyReport.DoesNotExist:
            daily_report = DailyReport(
                country=country,
                state=state,
                date=execution_date,
                confirmed=get_value(entries, Columns.CONFIRMED, convert_fct=int),
                deaths=get_value(entries, Columns.DEATHS, convert_fct=int),
                recovered=get_value(entries, Columns.RECOVERED, convert_fct=int),
            )
        daily_report.save()
