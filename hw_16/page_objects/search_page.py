from selenium.webdriver.common.by import By

from hw_16.utilities.ui_utilities.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __search_form = (By.XPATH, "//input[@name='search']")
    __search_button_main = (By.CSS_SELECTOR, "#searchform > div > button")
    __search_button_de = (By.CSS_SELECTOR, "#searchButton")
    __language_checkbox = (By.CSS_SELECTOR, "#p-lang-btn")
    __deutsch_language = (By.XPATH, '//a[@lang="de"][@dir="ltr"]')
    __ukrainian_language = (By.XPATH, '//a[@lang="uk"]')
    __italiano_language = (By.XPATH, '//a[@lang="it"]')

    def set_searching_data(self, searching_data):
        self.send_keys(self.__search_form, searching_data)
        return self

    def click_search_button_main(self):
        self.click(self.__search_button_main)
        return self

    def click_search_button_de_ua(self):
        self.click(self.__search_button_de)
        return self

    def click_on_lang_checkbox(self):
        self.click(self.__language_checkbox)
        self.click(self.__language_checkbox)

        return self

    def choose_deutsch_lang(self):
        self.click(self.__deutsch_language)
        return self

    def choose_ukrainian_lang(self):
        self.click(self.__ukrainian_language)
        return self

    def choose_italiano_lang(self):
        self.click(self.__italiano_language)
        return self
