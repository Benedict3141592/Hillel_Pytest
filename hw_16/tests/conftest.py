import json
import pytest

from hw_16.api_collections.data_classes.booking_data import Booking
from hw_16.api_collections.booking_api import BookingAPI
from hw_16.constans import ROOT_DIR
from hw_16.utilities.config_reader_json import ConfigReaderJson
from hw_16.utilities.driver_factory import create_driver_factory


@pytest.fixture()
def env():
    with open(f"{ROOT_DIR}/configurations/env.json") as file:
        file_data = file.read()
        json_data = json.loads(file_data)
        return ConfigReaderJson(**json_data)


@pytest.fixture()
def create_driver(env):
    driver = create_driver_factory(env.browser_id)
    driver.maximize_window()
    driver.get(env.base_url)
    yield driver
    driver.quit()


@pytest.fixture()
def create_donation_driver(env):
    driver = create_driver_factory(env.browser_id)
    driver.maximize_window()
    driver.get(env.donation_url)
    yield driver
    driver.quit()


@pytest.fixture()
def create_mock_booking(env):
    mock_data = BookingAPI(env).get_booking_by_id()
    booking = Booking(**mock_data.json())
    return booking
