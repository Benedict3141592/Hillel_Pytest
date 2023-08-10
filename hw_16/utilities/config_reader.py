import configparser
from hw_16.constans import ROOT_DIR

config = configparser.RawConfigParser()
config.read(f"{ROOT_DIR}/configurations/app_config.ini")


class ReadConfig:

    @staticmethod
    def get_browser_id():
        return config.get("browser_data", "browser_id")

    @staticmethod
    def get_base_url():
        return config.get("app_data", "base_url")

    @staticmethod
    def get_donation_url():
        return config.get("app_data", "donation_url")

    @staticmethod
    def get_login_url():
        return config.get("app_data", "login_url")

    @staticmethod
    def get_create_account_url():
        return config.get("app_data", "create_account_url")

    @staticmethod
    def get_user_data():
        return config.get("user_data", "login"), config.get("user_data", "password")

    @staticmethod
    def get_invalid_user_name():
        return config.get("user_data", "invalid_login"), config.get("user_data", "password")

    @staticmethod
    def get_invalid_password():
        return config.get("user_data", "login"), config.get("user_data", "invalid_password")

    @staticmethod
    def get_searching_data():
        return config.get("searching_data", "search_ruscism"), config.get("searching_data", "search_selenium"), \
            config.get("searching_data", "search_ukraine"), config.get("searching_data", "search_sheva"),

    @staticmethod
    def get_invalid_searching_data():
        return config.get("searching_data", "invalid_request")

    @staticmethod
    def get_supplement_searching_data():
        return config.get("searching_data", "search_swiss"), config.get("searching_data", "search_swiss_supplement")

    @staticmethod
    def get_cyrillic_searching_data():
        return config.get("searching_data", "search_cyrillic")

    @staticmethod
    def get_card_info():
        return config.get("card_info", "card_number"), config.get("card_info", "expiration_date"), \
            config.get("card_info", "security_code")

    @staticmethod
    def get_personal_info():
        return config.get("personal_details", "first_name"), config.get("personal_details", "last_name"), \
            config.get("personal_details", "email")

    @staticmethod
    def get_personal_info_via_invalid_email():
        return config.get("personal_details", "first_name"), config.get("personal_details", "last_name"), \
            config.get("personal_details", "invalid_email")

    @staticmethod
    def get_address_info():
        return config.get("address_details", "street"), config.get("address_details", "postal_code"), \
            config.get("address_details", "city")

    @staticmethod
    def get_download_folder_path():
        return config.get("download_folder", "path")

    @staticmethod
    def get_create_account_via_valid_username():
        return config.get("create_account_data", "create_valid_username")

    @staticmethod
    def get_create_account_invalid_username():
        return config.get("create_account_data", "create_invalid_username")

    @staticmethod
    def get_create_account_exist_username():
        return config.get("create_account_data", "create_exist_username")

    @staticmethod
    def get_create_account_invalid_password():
        return config.get("create_account_data", "create_invalid_password")

    @staticmethod
    def get_create_account_common_password():
        return config.get("create_account_data", "create_common_password")

    @staticmethod
    def get_create_account_invalid_common_password():
        return config.get("create_account_data", "create_invalid_common_password")
