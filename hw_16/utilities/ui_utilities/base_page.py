from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)

    def __wait_until_element_visible(self, locator: tuple):
        return self._wait.until(ec.visibility_of_element_located(locator))

    def __wait_until_element_clickable(self, locator: tuple):
        return self._wait.until(ec.element_to_be_clickable(locator))

    def send_keys(self, locator, value):
        element = self.__wait_until_element_visible(locator)
        element.clear()
        element.send_keys(value)

    def click(self, locator):
        self.__wait_until_element_clickable(locator).click()

    def is_displayed(self, locator):
        return self._wait.until(ec.presence_of_element_located(locator)).is_displayed()
