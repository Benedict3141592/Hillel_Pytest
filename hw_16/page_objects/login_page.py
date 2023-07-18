from selenium.webdriver.common.by import By

from hw_16.page_objects.main_page import MainPage
from hw_16.utilities.ui_utilities.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __login_input = (By.CSS_SELECTOR, "#wpName1")
    __password_input = (By.CSS_SELECTOR, "#wpPassword1")
    __login_button = (By.CSS_SELECTOR, "#wpLoginAttempt")

    def set_login(self, login_value):
        self.send_keys(self.__login_input, login_value)
        return self

    def set_password(self, password_value):
        self.send_keys(self.__password_input, password_value)
        return self

    def click_login_button(self):
        self.click(self.__login_button)
        return MainPage(self._driver)
