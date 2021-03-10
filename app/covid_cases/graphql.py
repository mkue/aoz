from ariadne import QueryType, make_executable_schema

from covid_cases.models import Country, DailyReport

type_defs = """
type Query{
    countries(id: Int): [Country]
    daily_reports(country_id: Int, from_date: String, to_date: String): [DailyReport]
}

type Country {
    id: ID
    name: String!
    state: State
    latitude: Float!
    longitude: Float!
}

type DailyReport {
    id: ID
    country: Country
    date: String!
    confirmed: Int
    deaths: Int
    recovered: Int
}

type State {
    id: ID
}
"""

query = QueryType()


@query.field("countries")
def resolve_countries(*_, id: int = None):
    if id:
        countries = Country.objects.filter(id=id)
    else:
        countries = Country.objects.all()
    return countries


@query.field("daily_reports")
def resolve_daily_reports(*_, country_id: int, from_date: str, to_date: str):
    return (
        DailyReport.objects.filter(country_id=country_id, date__gte=from_date, date__lte=to_date).order_by("date").all()
    )


schema = make_executable_schema(type_defs, query)
