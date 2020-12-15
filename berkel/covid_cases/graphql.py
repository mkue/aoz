from ariadne import QueryType, make_executable_schema

from covid_cases.models import Country, DailyReport

type_defs = """
type Query{
    countries: [Country]
    daily_reports: [DailyReport]
}

type Country {
    id: ID
    name: String!
    latitude: Float!
    longitude: Float!
}

type DailyReport {
    id: ID
    country: Country
}
"""

query = QueryType()


@query.field('countries')
def resolve_schools(*_):
    return Country.objects.all()


@query.field('daily_reports')
def resolve_schools(*_):
    return DailyReport.objects.all()


schema = make_executable_schema(type_defs, query)
