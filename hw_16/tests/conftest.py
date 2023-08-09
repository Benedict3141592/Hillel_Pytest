import json
import pytest

from hw_16.constans import ROOT_DIR
from hw_16.utilities.config_reader_json import ConfigReaderJson
from hw_16.page_objects.create_page import CreatePage
from hw_16.page_objects.login_page import LoginPage
from hw_16.page_objects.main_page import MainPage
from hw_16.page_objects.search_page import SearchPage
from hw_16.utilities.config_reader import ReadConfig
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
    driver.get(request.param)
    yield driver
    driver.quit()


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
