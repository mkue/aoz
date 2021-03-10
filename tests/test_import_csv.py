from datetime import date

import pytest

from covid_cases.models import DailyReport
from covid_cases.tasks import import_csv_file, _run_daily_import


@pytest.mark.django_db
@pytest.mark.parametrize(
    "execution_date, expected_count_switzerland_confirmed",
    [
        (date(month=12, day=12, year=2020), 373831),
        (date(month=12, day=13, year=2020), 373831),
        (date(month=12, day=14, year=2020), 384557),
        (date(month=12, day=15, year=2020), 388828),
        (date(month=12, day=16, year=2020), 394453),
        (date(month=12, day=17, year=2020), 399511),
        (date(month=12, day=18, year=2020), 403989),
    ],
)
def test_import_csv_file(execution_date: date, expected_count_switzerland_confirmed: int):
    _run_daily_import(execution_date)

    assert (
            DailyReport.objects.get(country__name="Switzerland", date=execution_date).confirmed
            == expected_count_switzerland_confirmed
    )
