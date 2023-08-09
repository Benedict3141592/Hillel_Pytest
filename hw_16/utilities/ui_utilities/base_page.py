from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Keys


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

    def send_keys_backspace(self, locator):
        return self.__wait_until_element_visible(locator).send_keys(Keys.BACKSPACE)

    def click(self, locator):
        self.__wait_until_element_clickable(locator).click()

    def get_back(self):
        self._driver.back()

    def is_displayed(self, locator):
        return self._wait.until(ec.presence_of_element_located(locator)).is_displayed()

    def get_text(self, locator):
        return self.__wait_until_element_visible(locator).text

    def get_attribute(self, locator, value):
        return self.__wait_until_element_visible(locator).get_attribute(value)

    def get_position(self, locator):
        return self.__wait_until_element_visible(locator).rect

    def get_css_value(self, locator, value):
        return self.__wait_until_element_visible(locator).value_of_css_property(value)

    def get_current_url(self):
        return self._driver.current_url
