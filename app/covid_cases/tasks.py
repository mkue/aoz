from datetime import datetime, date, timedelta

import requests
from huey import crontab
from huey.contrib.djhuey import db_periodic_task
from requests import HTTPError

from covid_cases import config
from covid_cases.importer import import_csv_file
from covid_cases.models import DailyReport, Country, State


def run_daily_import(execution_date: date = None):
    if not execution_date:
        execution_date = datetime.now().date() - timedelta(days=1)

    print(f"Importing date {execution_date}")
    r = requests.get(f"{config.csv_source_base_url}/{execution_date.strftime('%m-%d-%Y')}.csv")
    try:
        r.raise_for_status()
    except HTTPError:
        print("CSV files is not available")
        return

    import_csv_file(r.text, execution_date)

    print(f"Total countries  in database: {Country.objects.all().count()}")
    print(f"Total states in database: {State.objects.all().count()}")
    print(f"Total daily reports in database: {DailyReport.objects.all().count()}")


@db_periodic_task(crontab(hour="*/8"))  # run three times a day
def run_daily_import_task():
    run_daily_import()
