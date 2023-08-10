from selenium.webdriver.common.by import By
import allure

from hw_16.utilities.ui_utilities.base_page import BasePage


class DonationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __amount_of_donation = (By.XPATH, "//label[@class='label-radio-block amount amount-100 md-ripple']")
    __choose_payment_method = (By.CSS_SELECTOR, "#payment_method-cc-widget")
    __card_number_input = (By.CSS_SELECTOR, "#cardno-widget")
    __expiration_date_input = (By.CSS_SELECTOR, "#exp-widget")
    __security_code_input = (By.CSS_SELECTOR, "#cvv-widget")
    __salutation_widget = (By.CSS_SELECTOR, "#stored_customer_salutation-widget")
    __salutation_option = (By.XPATH, "//option[text()='Mr']")
    __first_name_input = (By.CSS_SELECTOR, "#stored_customer_firstname-widget")
    __last_name_input = (By.CSS_SELECTOR, "#stored_customer_lastname-widget")
    __email_input = (By.CSS_SELECTOR, "#stored_customer_email-widget")
    __street_input = (By.CSS_SELECTOR, "#stored_customer_street-widget")
    __postal_code_input = (By.CSS_SELECTOR, "#stored_customer_zip_code-widget")
    __city_input = (By.CSS_SELECTOR, "#stored_customer_city-widget")
    __country_widget = (By.CSS_SELECTOR, "#stored_customer_country-widget")
    __country_usa = (By.XPATH, '//option[@value="US"]')
    __state_widget = (By.CSS_SELECTOR, "#stored_customer_state-widget")
    __state_option_dc = (By.XPATH, '//option[@value="DC"]')
    __transmit_donation_button = (By.XPATH, "//button[@class='btn btn-block btn-primary md-ripple']")
    __card_error_message = (By.CSS_SELECTOR, "#cardno-error-widget")
    __expiration_date_error_message = (By.CSS_SELECTOR, "#exp-error-widget")
    __email_error_message = (By.CSS_SELECTOR, "#stored_customer_email-error-widget")
    __attribute_value = "value"

    @allure.step
    def choose_amount_of_donation(self):
        self.click(self.__amount_of_donation)
        return self

    @allure.step
    def choose_payment_method(self):
        self.click(self.__choose_payment_method)
        return self

    @allure.step
    def set_card_number(self, card_number):
        self.send_keys(self.__card_number_input, card_number)
        return self

    @allure.step
    def set_expiration_date(self, expiration_date):
        self.send_keys(self.__expiration_date_input, expiration_date)
        return self

    @allure.step
    def set_security_code(self, security_code):
        self.send_keys(self.__security_code_input, security_code)
        return self

    @allure.step
    def erase_one_letter_svv(self):
        self.send_keys_backspace(self.__security_code_input)
        return self

    @allure.step
    def click_on_salutation(self):
        self.click(self.__salutation_widget)
        return self

    @allure.step
    def choose_salutation_option(self):
        self.click(self.__salutation_option)
        return self

    @allure.step
    def set_first_name(self, first_name):
        self.send_keys(self.__first_name_input, first_name)
        return self

    @allure.step
    def set_last_name(self, last_name):
        self.send_keys(self.__last_name_input, last_name)
        return self

    @allure.step
    def set_email(self, email):
        self.send_keys(self.__email_input, email)
        return self

    @allure.step
    def set_street(self, street):
        self.send_keys(self.__street_input, street)
        return self

    @allure.step
    def set_postal_code(self, postal_code):
        self.send_keys(self.__postal_code_input, postal_code)
        return self

    @allure.step
    def set_city(self, city):
        self.send_keys(self.__city_input, city)
        return self

    @allure.step
    def click_on_country_widget(self):
        self.click(self.__country_widget)
        return self

    @allure.step
    def choose_country(self):
        self.click(self.__country_usa)
        return self

    @allure.step
    def click_on_state_widget(self):
        self.click(self.__state_widget)
        return self

    @allure.step
    def choose_state(self):
        self.click(self.__state_option_dc)
        return self

    @allure.step
    def transmit_donation(self):
        self.click(self.__transmit_donation_button)

    @allure.step
    def is_card_value_error_message(self):
        return self.get_text(self.__card_error_message)

    @allure.step
    def is_expiration_date_error_message(self):
        return self.get_text(self.__expiration_date_error_message)

    @allure.step
    def is_email_error_message(self):
        return self.get_text(self.__email_error_message)

    @allure.step
    def is_street_name_valid(self):
        return self.get_attribute(self.__street_input, self.__attribute_value)

    @allure.step
    def is_postal_code_valid(self):
        return self.get_attribute(self.__postal_code_input, self.__attribute_value)

    @allure.step
    def is_city_name_valid(self):
        return self.get_attribute(self.__city_input, self.__attribute_value)

    @allure.step
    def is_first_name_valid(self):
        return self.get_attribute(self.__first_name_input, self.__attribute_value)

    @allure.step
    def is_last_name_valid(self):
        return self.get_attribute(self.__last_name_input, self.__attribute_value)

    @allure.step
    def is_email_valid(self):
        return self.get_attribute(self.__email_input, self.__attribute_value)
