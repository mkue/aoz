from covid_cases.models import Country


def getcountry():
    country_list = Country.objects.all()
    for country in country_list:
        print(country.name)


getcountry()

