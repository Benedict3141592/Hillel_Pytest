import pytest
from hw_16.page_objects.donation_page import DonationPage
from hw_16.utilities.config_reader import ReadConfig


@pytest.mark.parametrize("create_driver", [ReadConfig.get_donation_url()], indirect=True)
def test_donation_page_set_invalid_payment_data(create_driver):
    card_number, expiration_date, cvv = ReadConfig.get_card_info()
    enter_card = DonationPage(create_driver)

    enter_card.choose_amount_of_donation().choose_payment_method().set_card_number(card_number). \
        set_expiration_date(expiration_date).set_security_code(cvv)

    assert enter_card.is_card_value_error_message() == "Card type not supported", "No card error message"
    assert enter_card.is_expiration_date_error_message() == "Expiration date invalid", \
        "No expiration date error message"


@pytest.mark.parametrize("create_driver", [ReadConfig.get_donation_url()], indirect=True)
def test_donation_page_set_valid_personal_data(create_driver):
    first_name, last_name, email = ReadConfig.get_personal_info()
    enter_personal_data = DonationPage(create_driver)

    enter_personal_data.click_on_salutation().choose_salutation_option().set_first_name(first_name). \
        set_last_name(last_name).set_email(email).transmit_donation()

    assert enter_personal_data.is_first_name_valid() == "Joe", "First name is not JOE"
    assert enter_personal_data.is_last_name_valid() == "Biden", "Last name is not Biden"
    assert enter_personal_data.is_email_valid() == "joe.biden@usa.gov", "Email is not joe.biden@usa.gov"


@pytest.mark.parametrize("create_driver", [ReadConfig.get_donation_url()], indirect=True)
def test_donation_page_set_invalid_email(create_driver):
    first_name, last_name, invalid_email = ReadConfig.get_personal_info_via_invalid_email()
    enter_personal_data = DonationPage(create_driver)

    enter_personal_data.click_on_salutation().choose_salutation_option().set_first_name(first_name). \
        set_last_name(last_name).set_email(invalid_email).transmit_donation()

    assert enter_personal_data.is_email_error_message() == "Please enter a valid e-mail address", \
        "No email error message"


@pytest.mark.parametrize("create_driver", [ReadConfig.get_donation_url()], indirect=True)
def test_donation_set_valid_address_data(create_driver):
    street, postal_code, city = ReadConfig.get_address_info()
    enter_address = DonationPage(create_driver)

    enter_address.set_street(street).set_postal_code(postal_code).set_city(city).click_on_country_widget(). \
        choose_country().click_on_state_widget().choose_state().transmit_donation()

    assert enter_address.is_street_name_valid() == "1600 Pennsylvania Avenue NW", "Alert! Wrong address"
    assert enter_address.is_postal_code_valid() == "DC 20500", "Alert! Wrong postal code"
    assert enter_address.is_city_name_valid() == "Washington", "Alert! Wrong city"


@pytest.mark.parametrize("create_driver", [ReadConfig.get_donation_url()], indirect=True)
def test_donation_page_must_be_valid_data(create_driver):
    card_number, expiration_date, cvv = ReadConfig.get_card_info()
    first_name, last_name, email = ReadConfig.get_personal_info()
    street, postal_code, city = ReadConfig.get_address_info()

    enter_card = enter_personal_data = enter_address = DonationPage(create_driver)

    enter_card.choose_amount_of_donation().choose_payment_method().set_card_number(card_number). \
        set_expiration_date(expiration_date).set_security_code(cvv)

    enter_personal_data.click_on_salutation().choose_salutation_option().set_first_name(first_name). \
        set_last_name(last_name).set_email(email)

    enter_address.set_street(street).set_postal_code(postal_code).set_city(city).click_on_country_widget(). \
        choose_country().click_on_state_widget().choose_state().transmit_donation()

    assert enter_card.is_card_value_error_message() == "Card type not supported", "Wrong error message"
