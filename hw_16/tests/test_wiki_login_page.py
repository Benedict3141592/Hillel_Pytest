import pytest
from hw_16.page_objects.login_page import LoginPage
from hw_16.page_objects.main_page import MainPage


@pytest.mark.parametrize("create_driver", [ReadConfig.get_base_url()], indirect=True)
def test_login(create_driver, env):
    user_name, password = env.login, env.password
    driver = create_driver

    MainPage(driver).click_to_login_page()
    main_page = LoginPage(driver).set_login(user_name).set_password(password).click_login_button_main_page()

    assert main_page.is_user_label_displayed(), "User label is not displayed"


@pytest.mark.parametrize("create_driver", [ReadConfig.get_login_url()], indirect=True)
def test_login_via_invalid_user_name(create_driver, login_page):
    user_name, password = ReadConfig.get_invalid_user_name()

    login_page.set_login(user_name).set_password(password).click_login_button_login_page()

    assert login_page.is_error_message_displayed() is True, "Error message not displayed"
    assert login_page.is_value_error_message() == "Incorrect username or password entered. Please try again.", \
        "No error message via invalid username"


@pytest.mark.parametrize("create_driver", [ReadConfig.get_login_url()], indirect=True)
def test_login_via_invalid_password(create_driver, login_page):
    user_name, password = ReadConfig.get_invalid_password()

    login_page.set_login(user_name).set_password(password).click_login_button_login_page()

    assert login_page.is_error_message_displayed() is True, "Error message not displayed"
    assert login_page.is_value_error_message() == "Incorrect username or password entered. Please try again.", \
        "No error message via invalid password"


@pytest.mark.parametrize("create_driver", [ReadConfig.get_login_url()], indirect=True)
def test_login_page_links_clickable(create_driver, login_page):
    login_page.click_help_with_logging()
    assert "Help:Logging in - MediaWiki" in create_driver.title, "Alert! Title is not 'Help:Logging in - MediaWiki'"
    login_page.get_back()
    assert "Log in - Wikipedia" in create_driver.title, "Alert! Title is not 'Log in - Wikipedia'"
    login_page.click_forgot_password()
    assert "Reset password - Wikipedia" in create_driver.title, "Alert! Title is not 'Reset password - Wikipedia'"
    login_page.get_back()
    assert "Log in - Wikipedia" in create_driver.title, "Alert! Title is not 'Log in - Wikipedia'"
    login_page.click_join_wikipedia()
    assert "Create account - Wikipedia" in create_driver.title, "Alert! Title is not 'Create account - Wikipedia'"


@pytest.mark.parametrize("create_driver", [ReadConfig.get_login_url()], indirect=True)
def test_login_data_in_elements(create_driver, login_page):
    user_name, password = ReadConfig.get_user_data()

    login_page.set_login(user_name)

    assert login_page.is_login_data_valid() == "QAutotest", "Alert! Wrong login data!"
