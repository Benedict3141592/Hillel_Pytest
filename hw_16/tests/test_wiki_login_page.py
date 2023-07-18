from hw_16.page_objects.login_page import LoginPage
from hw_16.page_objects.main_page import MainPage
from hw_16.utilities.config_reader import ReadConfig


def test_login(create_driver):
    user_name, password = ReadConfig.get_user_data()
    driver = create_driver

    MainPage(driver).click_to_login_page()

    main_page = LoginPage(driver).set_login(user_name).set_password(password).click_login_button()

    assert main_page.is_user_label_displayed(), "User label is not displayed"
