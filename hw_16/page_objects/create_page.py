from selenium.webdriver.common.by import By

from hw_16.utilities.ui_utilities.base_page import BasePage


class CreatePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __username_input = (By.CSS_SELECTOR, "#wpName2")
    __error_message = (By.XPATH, "//div[@class='mw-message-box mw-message-box-error']")
    __password_input = (By.CSS_SELECTOR, "#wpPassword2")

    def set_invalid_username(self, username):
        self.send_keys(self.__username_input, username)
        return self

    def set_exist_username(self, username):
        self.send_keys(self.__username_input, username)
        return self

    def set_valid_username(self, username):
        self.send_keys(self.__username_input, username)
        return self

    def set_invalid_password(self, password):
        self.send_keys(self.__password_input, password)
        return self

    def set_common_password(self, password):
        self.send_keys(self.__password_input, password)
        return self

    def set_invalid_common_password(self, password):
        self.send_keys(self.__password_input, password)
        return self

    def is_username_error_message(self):
        return self.get_text(self.__error_message)

    def is_username_exist_message(self):
        return self.get_text(self.__error_message)

    def is_password_error_message(self):
        return self.get_text(self.__error_message)
