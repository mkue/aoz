import os
from abc import ABC
from dataclasses import dataclass

from django.apps import AppConfig

DEVELOPMENT = "development"
TESTING = "testing"
PRODUCTION = "production"


@dataclass(frozen=True)
class DefaultConfig(ABC):
    csv_source_base_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports"


@dataclass(frozen=True)
class DevConfig(AppConfig):
    csv_source_base_url = "http://file-server"


@dataclass(frozen=True)
class TestConfig(AppConfig):
    csv_source_base_url = "http://file-server"


@dataclass(frozen=True)
class ProdConfig(AppConfig):
    pass


ENV_CONFIG_MAP = {DEVELOPMENT: DevConfig, TESTING: DevConfig, PRODUCTION: ProdConfig}

app_mode = os.environ["APP_MODE"] or DEVELOPMENT
config = ENV_CONFIG_MAP.get(app_mode.lower())
