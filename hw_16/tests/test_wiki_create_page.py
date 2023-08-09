import pytest
from hw_16.utilities.config_reader import ReadConfig


@pytest.mark.parametrize("create_driver", [ReadConfig.get_create_account_url()], indirect=True)
def test_create_page_via_invalid_username(create_driver, create_page):
    invalid_username = ReadConfig.get_create_account_invalid_username()

    create_page.set_invalid_username(invalid_username)

    assert create_page.is_username_error_message() == "You have not specified a valid user name.", \
        "Test create page via invalid username wrong error message"


@pytest.mark.parametrize("create_driver", [ReadConfig.get_create_account_url()], indirect=True)
def test_create_page_via_exist_username(create_driver, create_page):
    exist_username = ReadConfig.get_create_account_exist_username()

    create_page.set_exist_username(exist_username)

    assert create_page.is_username_error_message() == ("Username entered already in use. Please choose a different name"
                                                       "."), "Test create page via exist username wrong error message"


@pytest.mark.parametrize("create_driver", [ReadConfig.get_create_account_url()], indirect=True)
def test_create_page_via_invalid_password(create_driver, create_page):
    valid_username = ReadConfig.get_create_account_via_valid_username()
    invalid_password = ReadConfig.get_create_account_invalid_password()

    create_page.set_valid_username(valid_username).set_invalid_password(invalid_password)

    assert create_page.is_password_error_message() == "Passwords must be at least 8 characters.", \
        "Test invalid password wrong error message"


@pytest.mark.parametrize("create_driver", [ReadConfig.get_create_account_url()], indirect=True)
def test_create_page_via_common_password(create_driver, create_page):
    valid_username = ReadConfig.get_create_account_via_valid_username()
    common_password = ReadConfig.get_create_account_common_password()

    create_page.set_valid_username(valid_username).set_common_password(common_password)

    assert create_page.is_password_error_message() == ("The password entered is in a list of very commonly used "
                                                       "passwords. Please choose a more unique password."), \
        "Test common password wrong error message"


@pytest.mark.parametrize("create_driver", [ReadConfig.get_create_account_url()], indirect=True)
def test_create_page_via_invalid_common_password(create_driver, create_page):
    valid_username = ReadConfig.get_create_account_via_valid_username()
    invalid_common_password = ReadConfig.get_create_account_invalid_common_password()

    create_page.set_valid_username(valid_username).set_invalid_common_password(invalid_common_password)

    assert create_page.is_password_error_message() == """Passwords must be at least 8 characters.
The password entered is in a list of very commonly used passwords. Please choose a more unique password.""", \
        "Test common and invalid password wrong error message"
