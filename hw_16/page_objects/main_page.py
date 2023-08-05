from selenium.webdriver.common.by import By
import os.path

from hw_16.utilities.ui_utilities.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __login_link = (By.CSS_SELECTOR, "#pt-login-2")
    __user_label = (By.XPATH, "//li[@id='pt-userpage-2']/a/span[text()='QAutotest']")
    __checkbox = (By.CSS_SELECTOR, "#vector-page-tools-dropdown")
    __download_as_pdf = (By.CSS_SELECTOR, "#coll-download-as-rl")
    __download_button = (By.CSS_SELECTOR, "#mw-content-text > form > div > span > span")

    def click_to_login_page(self):
        self.click(self.__login_link)

    def is_user_label_displayed(self):
        return self.is_displayed(self.__user_label)

    def click_to_open_checkbox(self):
        self.click(self.__checkbox)
        return self

    def click_to_download_page(self):
        self.click(self.__download_as_pdf)
        return self

    def click_download_button(self):
        self.click(self.__download_button)
        return self

    @staticmethod
    def is_file_in_folder(path):
        return os.path.exists(path) and os.path.isfile(path)

    @staticmethod
    def delete_file(path):
        return os.remove(path)
