from hw_16.page_objects.donation_page import DonationPage


def test_donation_page(create_donation_driver, env):
    card_number, expiration_date, cvv = env.card_number, env.expiration_date, env.security_code
    first_name, last_name, email = env.first_name, env.last_name, env.email
    street, postal_code, city = env.street, env.postal_code, env.city
    driver = create_donation_driver

    DonationPage(driver).choose_amount_of_donation().choose_payment_method().set_card_number(card_number). \
        set_expiration_date(expiration_date).set_security_code(cvv).click_on_salutation().choose_salutation_option(). \
        set_first_name(first_name).set_last_name(last_name).set_email(email).set_street(street). \
        set_postal_code(postal_code).set_city(city).click_on_country_widget().choose_country().click_on_state_widget(). \
        choose_state().transmit_donation()
    assert DonationPage(driver).check_error_message(), "No error message"
