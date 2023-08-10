import json
import pytest

from hw_16.api_collections.data_classes.booking_data import Booking
from hw_16.api_collections.booking_api import BookingAPI
from hw_16.constans import ROOT_DIR
from hw_16.utilities.config_reader_json import ConfigReaderJson
from hw_16.page_objects.create_page import CreatePage
from hw_16.page_objects.login_page import LoginPage
from hw_16.page_objects.main_page import MainPage
from hw_16.page_objects.search_page import SearchPage
from hw_16.utilities.driver_factory import create_driver_factory


@pytest.fixture()
def env():
    with open(f"{ROOT_DIR}/configurations/env.json") as file:
        file_data = file.read()
        json_data = json.loads(file_data)
        return ConfigReaderJson(**json_data)


@pytest.fixture()
def create_driver(request, env):
    driver = create_driver_factory(env.browser_id)
    driver.maximize_window()
    driver.get(eval(request.param))
    yield driver
    driver.quit()


@pytest.fixture()
def create_mock_booking(env):
    mock_data = BookingAPI(env).get_booking_by_id(1)
    booking = Booking(**mock_data.json())
    return booking


@pytest.fixture()
def search_page(create_driver):
    driver = create_driver
    yield SearchPage(driver)


@pytest.fixture()
def create_page(create_driver):
    driver = create_driver
    yield CreatePage(driver)


@pytest.fixture()
def login_page(create_driver):
    driver = create_driver
    yield LoginPage(driver)


@pytest.fixture()
def main_page(create_driver):
    driver = create_driver
    yield MainPage(driver)
