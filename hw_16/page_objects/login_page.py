from selenium.webdriver.common.by import By
import allure

from hw_16.page_objects.main_page import MainPage
from hw_16.utilities.ui_utilities.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __login_input = (By.CSS_SELECTOR, "#wpName1")
    __password_input = (By.CSS_SELECTOR, "#wpPassword1")
    __login_button = (By.CSS_SELECTOR, "#wpLoginAttempt")
    __error_message = (By.XPATH, "//div[@class='cdx-message__content']")
    __help_logging_link = (By.XPATH, "//div[@class='mw-input mw-htmlform-nolabel']/a[text()='Help with logging in']")
    __forgot_password_link = (By.CSS_SELECTOR, "a[title='Special:PasswordReset']")
    __join_wikipedia_link = (By.CSS_SELECTOR, "#mw-createaccount-join")
    __attribute_value = "value"

    @allure.step
    def set_login(self, login_value):
        self.send_keys(self.__login_input, login_value)
        return self

    @allure.step
    def set_password(self, password_value):
        self.send_keys(self.__password_input, password_value)
        return self

    @allure.step
    def click_login_button_main_page(self):
        self.click(self.__login_button)
        return MainPage(self._driver)

    @allure.step
    def click_login_button_login_page(self):
        self.click(self.__login_button)
        return LoginPage(self._driver)

    @allure.step
    def click_help_with_logging(self):
        self.click(self.__help_logging_link)

    @allure.step
    def click_forgot_password(self):
        self.click(self.__forgot_password_link)

    @allure.step
    def click_join_wikipedia(self):
        self.click(self.__join_wikipedia_link)

    @allure.step
    def is_error_message_displayed(self):
        return self.is_displayed(self.__error_message)

    @allure.step
    def is_value_error_message(self):
        return self.get_text(self.__error_message)

    @allure.step
    def is_login_data_valid(self):
        return self.get_attribute(self.__login_input, self.__attribute_value)
