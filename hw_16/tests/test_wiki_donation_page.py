from hw_16.page_objects.donation_page import DonationPage
from hw_16.utilities.config_reader import ReadConfig


def test_donation_page(create_donation_driver):
    card_number, expiration_date, cvv = ReadConfig.get_card_info()
    first_name, last_name, email = ReadConfig.get_personal_info()
    driver = create_donation_driver
    street, postal_code, city = ReadConfig.get_address_info()

    DonationPage(driver).choose_amount_of_donation().choose_payment_method().set_card_number(card_number). \
        set_expiration_date(expiration_date).set_security_code(cvv).click_on_salutation().choose_salutation_option(). \
        set_first_name(first_name).set_last_name(last_name).set_email(email).set_street(street). \
        set_postal_code(postal_code).set_city(city).click_on_country_widget().choose_country().click_on_state_widget().\
        choose_state().transmit_donation()
    assert DonationPage(driver).check_error_message(), "No error message"
