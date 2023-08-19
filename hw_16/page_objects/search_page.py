from selenium.webdriver.common.by import By
import allure
import time

from hw_16.utilities.ui_utilities.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __search_form = (By.CSS_SELECTOR, "input[name='search']")
    __search_button_main = (By.CSS_SELECTOR, "#searchform > div > button")
    __search_button_de = (By.CSS_SELECTOR, "#searchButton")
    __language_checkbox = (By.CSS_SELECTOR, "#p-lang-btn")
    __deutsch_language = (By.XPATH, '//a[@lang="de"][@dir="ltr"]')
    __france_language = (By.XPATH, '//a[@lang="fr"]')
    __italiano_language = (By.XPATH, '//a[@lang="it"]')
    __search_not_found = (By.XPATH, "//*[@id='mw-content-text']/div[3]/div[1]/p[1]")
    __search_found = (By.XPATH, "//*[@id='mw-content-text']/div[3]/div[1]/p/b")
    __advanced_search_list = (By.CSS_SELECTOR, "a[aria-controls='mw-advancedSearch-expandable-options']")
    __these_words_input = (By.CSS_SELECTOR, "#ooui-33")
    __search_button = (By.CSS_SELECTOR, "button[value]")
    __search_input = (By.CSS_SELECTOR, "#ooui-php-1")
    __attribute_value = "value"
    __title_value = (By.CSS_SELECTOR, "span[class='mw-page-title-main']")

    @allure.step
    def set_searching_data(self, searching_data):
        self.send_keys(self.__search_form, searching_data)
        return self

    @allure.step
    def click_search_button_main(self):
        self.click(self.__search_button_main)
        return self

    @allure.step
    def click_search_button_de_ua(self):
        self.click(self.__search_button_de)
        return self

    @allure.step
    def click_on_lang_checkbox(self):
        self.click(self.__language_checkbox)
        return self

    @allure.step
    def choose_deutsch_lang(self):
        self.click(self.__deutsch_language)
        return self

    @allure.step
    def choose_france_lang(self):
        self.click(self.__france_language)
        return self

    @allure.step
    def choose_italiano_lang(self):
        self.click(self.__italiano_language)
        return self

    @allure.step
    def click_advanced_search_list(self):
        self.click(self.__advanced_search_list)
        return self

    @allure.step
    def set_supplement_data(self, request):
        self.send_keys(self.__these_words_input, request)
        return self

    @allure.step
    def click_search_button(self):
        self.click(self.__search_button)
        return self

    @allure.step
    def is_request_not_found(self):
        return self.get_text(self.__search_not_found)

    @allure.step
    def is_request_found(self):
        return self.get_text(self.__search_found)

    @allure.step
    def is_value_empty(self):
        return self.get_attribute(self.__search_input, self.__attribute_value)

    @allure.step
    def is_title_correct(self):
        return self.get_text(self.__title_value)

    @staticmethod
    def wait_loading(timeout=10, interval=0.1):
        start_time = time.time()
        while time.time() - start_time < 0.7:
            if time.time() - start_time >= timeout:
                raise TimeoutError("Timeout error.")
            time.sleep(interval)
