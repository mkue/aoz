from sqlite3.dbapi2 import Date


class DailyReportDetails():
    def __init__(self, country_name, deaths, confirmed):
        self.country_name: country_name
        self.deaths: deaths
        self.confirmed: confirmed
