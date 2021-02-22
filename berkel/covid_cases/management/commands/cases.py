
import csv
import logging
from datetime import datetime

import requests
from django.db.transaction import atomic

from covid_cases.management.controller import out_cases
from covid_cases.models import Country, State, DailyReport

from django.core.management import BaseCommand

class Command(BaseCommand):

   def handle(self, *args, **options):

    out_cases.getcountry()