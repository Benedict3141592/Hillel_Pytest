from hw_16.page_objects.search_page import SearchPage
from hw_16.utilities.config_reader import ReadConfig


def test_search_option(create_driver):
    driver = create_driver
    ruscism, selenium, ukraine, sheva = ReadConfig.get_searching_data()
    search_page = SearchPage(driver)
    search_page.set_searching_data(ruscism).click_search_button_main()
    assert "Ruscism - Wikipedia" in driver.title
    search_page.set_searching_data(selenium).click_search_button_main().click_on_lang_checkbox().choose_deutsch_lang()
    assert "Selen – Wikipedia" in driver.title
    search_page.set_searching_data(ukraine).click_search_button_de_ua().choose_ukrainian_lang()
    assert "Україна — Вікіпедія" in driver.title
    search_page.choose_italiano_lang().set_searching_data(sheva).click_search_button_de_ua()
    assert "Andrij Ševčenko - Wikipedia" in driver.title
