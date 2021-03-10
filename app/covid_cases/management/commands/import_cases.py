from datetime import datetime

from django.core.management import BaseCommand
from django.db.transaction import atomic

from covid_cases.tasks import run_daily_import


class Command(BaseCommand):
    help = "Import new Covid-19 cases"

    def add_arguments(self, parser):
        parser.add_argument("date", nargs="?", default="2020-03-24")

    @atomic
    def handle(self, *args, **options):
        execution_date = datetime.strptime(options["date"], "%Y-%m-%d").date()
        run_daily_import(execution_date)
