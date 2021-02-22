from ariadne import QueryType, make_executable_schema
from covid_cases.dto import DailyReportDetails

from covid_cases.models import Country, DailyReport

type_defs = """
type Query{
    countries: [Country]
    daily_reports: [DailyReport]
    dailyreportsdeatils: DailyReportDetails
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
    confirmed:Int!
    deaths:Int!
    date:String!
}

type DailyReportDetails{
  country_name: String!
  confirmed: Int!
}
"""

query = QueryType()


@query.field('countries')
def resolve_schools(*_):
    return Country.objects.all()


@query.field('daily_reports')
def resolve_schools(*_):
    return DailyReport.objects.all()


@query.field('dailyreportsdeatils')
def resolve_schools(*_):
    # data = DailyReport.objects.filter(date='2020-03-24', country=Country.objects.get(name='Switzerland'))
    data = DailyReport.objects.filter(date='2020-03-24', country=Country.objects.get(name='Switzerland')).first()
    model = DailyReportDetails(country_name=data.country.name, deaths=data.deaths, confirmed=data.confirmed)
    return model


schema = make_executable_schema(type_defs, query)
