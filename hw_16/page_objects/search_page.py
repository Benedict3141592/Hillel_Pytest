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
    __search_not_found = (By.XPATH, "//*[@id='mw-content-text']/div[3]/div[1]/p[1]")
    __search_found = (By.XPATH, "//*[@id='mw-content-text']/div[3]/div[1]/p/b")
    __advanced_search_list = (By.CSS_SELECTOR, "a[aria-controls='mw-advancedSearch-expandable-options']")
    __these_words_input = (By.CSS_SELECTOR, "#ooui-33")
    __search_button = (By.CSS_SELECTOR, "button[value]")
    __search_input = (By.CSS_SELECTOR, "#ooui-php-1")
    __attribute_value = "value"
    __title_value = (By.CSS_SELECTOR, "span[class='mw-page-title-main']")

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

    def click_advanced_search_list(self):
        self.click(self.__advanced_search_list)
        return self

    def set_supplement_data(self, request):
        self.send_keys(self.__these_words_input, request)
        return self

    def click_search_button(self):
        self.click(self.__search_button)
        return self

    def is_request_not_found(self):
        return self.get_text(self.__search_not_found)

    def is_request_found(self):
        return self.get_text(self.__search_found)

    def is_value_empty(self):
        return self.get_attribute(self.__search_input, self.__attribute_value)

    def is_title_correct(self):
        return self.get_text(self.__title_value)
