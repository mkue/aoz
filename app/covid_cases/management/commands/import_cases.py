from datetime import datetime, timedelta

from django.core.management import BaseCommand
from django.db.transaction import atomic

from covid_cases.tasks import run_daily_import

FROM_DATE_ARG = "from_date"
TO_DATE_ARG = "to_date"


class Command(BaseCommand):
    help = "Import new Covid-19 cases"

    def add_arguments(self, parser):
        parser.add_argument(FROM_DATE_ARG, nargs="?", default=None)
        parser.add_argument(TO_DATE_ARG, nargs="?", default=None)

    @atomic
    def handle(self, *args, **options):
        if not options[FROM_DATE_ARG]:  # no from_date passed, run with no parameter
            run_daily_import()
            return

        from_date = datetime.strptime(options[FROM_DATE_ARG], "%Y-%m-%d").date()

        if not options[TO_DATE_ARG]:  # no to_date passed, run only with from_date
            run_daily_import(from_date)
            return

        # if from_date and to_date parameter where passed we run import on every day
        to_date = datetime.strptime(options[TO_DATE_ARG], "%Y-%m-%d").date()
        delta = to_date - from_date
        for i in range(delta.days + 1):
            run_daily_import(from_date + timedelta(days=i))
