import configparser
from hw_16.constans import ROOT_DIR

config = configparser.RawConfigParser()
config.read(f"{ROOT_DIR}/configurations/app_config.ini")


class ReadConfig:

    @staticmethod
    def get_browser_id():
        return config.get("browser_data", "browser_id")

    @staticmethod
    def get_app_base_url():
        return config.get("app_data", "base_url")

    @staticmethod
    def get_app_donation_url():
        return config.get("app_data", "donation_url")

    @staticmethod
    def get_user_data():
        return config.get("user_data", "login"), config.get("user_data", "password")

    @staticmethod
    def get_searching_data():
        return config.get("searching_data", "search_ruscism"), config.get("searching_data", "search_selenium"), \
            config.get("searching_data", "search_ukraine"), config.get("searching_data", "search_sheva"),

    @staticmethod
    def get_card_info():
        return config.get("card_info", "card_number"), config.get("card_info", "expiration_date"), \
            config.get("card_info", "security_code")

    @staticmethod
    def get_personal_info():
        return config.get("personal_details", "first_name"), config.get("personal_details", "last_name"), \
            config.get("personal_details", "email")

    @staticmethod
    def get_address_info():
        return config.get("address_details", "street"), config.get("address_details", "postal_code"), \
            config.get("address_details", "city")

    @staticmethod
    def get_download_folder_path():
        return config.get("download_folder","path")
