from hw_16.page_objects.main_page import MainPage


def test_main_page(create_driver, env):
    file_path = env.path
    driver = create_driver
    main = MainPage(driver)
    main.click_to_open_checkbox().click_to_download_page().click_download_button()
    assert main.verify_file(file_path), "File not in the folder"
    main.delete_file(file_path)
