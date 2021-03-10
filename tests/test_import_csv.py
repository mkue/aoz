from datetime import date

import pytest

from covid_cases.models import DailyReport
from covid_cases.tasks import import_csv_file


@pytest.mark.django_db
@pytest.mark.parametrize(
    "file_path, execution_date, expected_count_switzerland_confirmed",
    [
        ("/tests/data/12-12-2020.csv", date(month=12, day=12, year=2020), 373831),
        ("/tests/data/12-13-2020.csv", date(month=12, day=13, year=2020), 373831),
        ("/tests/data/12-14-2020.csv", date(month=12, day=14, year=2020), 384557),
        ("/tests/data/12-15-2020.csv", date(month=12, day=15, year=2020), 388828),
        ("/tests/data/12-16-2020.csv", date(month=12, day=16, year=2020), 394453),
        ("/tests/data/12-17-2020.csv", date(month=12, day=17, year=2020), 399511),
        ("/tests/data/12-18-2020.csv", date(month=12, day=18, year=2020), 403989),
    ],
)
def test_import_csv_file(file_path: str, execution_date: date, expected_count_switzerland_confirmed: int):
    with open(file_path, mode="r") as f:
        import_csv_file(f.read(), execution_date)
    assert (
        DailyReport.objects.get(country__name="Switzerland", date=execution_date).confirmed
        == expected_count_switzerland_confirmed
    )
