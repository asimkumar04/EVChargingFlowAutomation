import pytest
import os
from datetime import datetime
from dotenv import load_dotenv
from api.poi_api import POIApi
from api.referencedata_api import ReferenceDataAPI

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")


@pytest.fixture(scope="session")
def poi_api():
    return POIApi(BASE_URL, API_KEY)

@pytest.fixture(scope="session")
def reference_api():
    return ReferenceDataAPI(BASE_URL, API_KEY)

def pytest_configure(config):
    # Ensure reports folder exists
    os.makedirs("reports", exist_ok=True)

    # Generate timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Set dynamic report path
    report_file = f"reports/report_{timestamp}.html"

    # Inject into pytest-html
    config.option.htmlpath = report_file
    config.option.self_contained_html = True