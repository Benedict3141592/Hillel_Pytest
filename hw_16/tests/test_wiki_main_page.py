from hw_16.page_objects.main_page import MainPage
from hw_16.utilities.config_reader import ReadConfig


def test_main_page(create_driver):
    file_path = ReadConfig.get_download_folder_path()
    driver = create_driver
    main = MainPage(driver)
    main.click_to_open_checkbox().click_to_download_page().click_download_button()
    assert main.is_file_in_folder(file_path), "File not in the folder"
    main.delete_file(file_path)
