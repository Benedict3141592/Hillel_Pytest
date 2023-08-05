import pytest

from hw_16.utilities.config_reader import ReadConfig
from hw_16.utilities.driver_factory import create_driver_factory


@pytest.fixture()
def create_driver(page_url):
    driver = create_driver_factory(ReadConfig.get_browser_id())
    driver.maximize_window()
    driver.get(ReadConfig.get_url(page_url))
    yield driver
    driver.quit()


@pytest.fixture()
def create_donation_driver():
    driver = create_driver_factory(ReadConfig.get_browser_id())
    driver.maximize_window()
    driver.get(ReadConfig.get_app_donation_url())
    yield driver
    driver.quit()
