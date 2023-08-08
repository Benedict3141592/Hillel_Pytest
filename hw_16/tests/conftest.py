import pytest

from hw_16.page_objects.create_page import CreatePage
from hw_16.page_objects.login_page import LoginPage
from hw_16.page_objects.main_page import MainPage
from hw_16.page_objects.search_page import SearchPage
from hw_16.utilities.config_reader import ReadConfig
from hw_16.utilities.driver_factory import create_driver_factory


@pytest.fixture()
def create_driver(request):
    driver = create_driver_factory(ReadConfig.get_browser_id())
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
