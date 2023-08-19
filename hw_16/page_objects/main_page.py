from selenium.webdriver.common.by import By
import allure
import os.path
import time

from hw_16.utilities.ui_utilities.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __login_link = (By.CSS_SELECTOR, "#pt-login-2")
    __user_label = (By.XPATH, "//li[@id='pt-userpage-2']/a/span[text()='QAutotest']")
    __checkbox = (By.CSS_SELECTOR, "#vector-page-tools-dropdown")
    __download_as_pdf = (By.CSS_SELECTOR, "#coll-download-as-rl")
    __download_button = (By.CSS_SELECTOR, "#mw-content-text > form > div > span > span")
    __sidebar_button = (By.CSS_SELECTOR, "#vector-main-menu-dropdown")
    __main_page_link = (By.XPATH, "//*[@id='n-mainpage-description']/a")
    __contents_link = (By.XPATH, "//*[@id='n-contents']/a")
    __currents_events = (By.XPATH, "//*[@id='n-currentevents']/a")
    __about_link = (By.XPATH, "//*[@id='n-aboutsite']/a")
    __wiki_logo_icon = (By.XPATH, "/html/body/div[1]/header/div[1]/a/img")
    __wiki_logo_container = (By.CSS_SELECTOR, "span[class='mw-logo-container']")
    __page_container = (By.CSS_SELECTOR, "div[class='mw-page-container']")
    __commons_page = (By.XPATH, "//*[@id='sister-projects-list']/li[1]/div[2]/span/a")
    __wikibooks_page = (By.XPATH, "//*[@id='sister-projects-list']/li[4]/div[2]/span/a")
    __mediawiki_page = (By.XPATH, '//*[@id="sister-projects-list"]/li[2]/div[2]/span/a')

    __css_value_background_color = "background-color"
    __css_value_font_family = "font-family"

    @allure.step
    def click_to_login_page(self):
        self.click(self.__login_link)

    @allure.step
    def is_user_label_displayed(self):
        return self.is_displayed(self.__user_label)

    @allure.step
    def click_to_open_checkbox(self):
        self.click(self.__checkbox)
        return self

    @allure.step
    def click_to_download_page(self):
        self.click(self.__download_as_pdf)
        return self

    @allure.step
    def click_download_button(self):
        self.click(self.__download_button)
        return self

    @allure.step
    def click_sidebar_menu(self):
        self.click(self.__sidebar_button)
        return self

    @allure.step
    def click_main_page_link(self):
        self.click(self.__main_page_link)
        return self

    @allure.step
    def click_contents_link(self):
        self.click(self.__contents_link)
        return self

    @allure.step
    def click_current_events_link(self):
        self.click(self.__currents_events)
        return self

    @allure.step
    def click_about_link(self):
        self.click(self.__about_link)
        return self

    @allure.step
    def click_common_page(self):
        self.click(self.__commons_page)
        return self

    @allure.step
    def click_wikibooks_page(self):
        self.click(self.__wikibooks_page)
        return self

    @allure.step
    def click_mediawiki_page(self):
        self.click(self.__mediawiki_page)
        return self

    @allure.step
    def is_wiki_logo_icon(self):
        return self.get_position(self.__wiki_logo_icon)

    @allure.step
    def is_wiki_logo_container(self):
        return self.get_position(self.__wiki_logo_container)

    @allure.step
    def is_css_value_background_color(self):
        return self.get_css_value(self.__page_container, self.__css_value_background_color)

    @allure.step
    def is_css_value_font_family(self):
        return self.get_css_value(self.__page_container, self.__css_value_font_family)

    @staticmethod
    def wait_file(path, timeout=10, interval=0.1):
        start_time = time.time()
        while os.path.isfile(path) is not True:
            if time.time() - start_time >= timeout:
                raise TimeoutError("Timeout error.")
            time.sleep(interval)

    @staticmethod
    def is_file_in_folder(path):
        return os.path.exists(path) and os.path.isfile(path)

    @staticmethod
    def delete_file(path):
        return os.remove(path)
