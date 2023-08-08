import pytest
from hw_16.page_objects.main_page import MainPage
from hw_16.utilities.config_reader import ReadConfig


@pytest.mark.parametrize("create_driver", [ReadConfig.get_base_url()], indirect=True)
def test_main_page_download_file(create_driver, main_page):
    file_path = ReadConfig.get_download_folder_path()

    main_page.click_to_open_checkbox().click_to_download_page().click_download_button()

    assert main_page.is_file_in_folder(file_path), "File not in the folder"
    main_page.delete_file(file_path)


@pytest.mark.parametrize("create_driver", [ReadConfig.get_base_url()], indirect=True)
def test_main_page_sidebar(create_driver, main_page):
    main_page.click_sidebar_menu().click_main_page_link()
    assert "Wikipedia, the free encyclopedia" in create_driver.title, "Wrong title in main page link"
    main_page.get_back()

    main_page.click_sidebar_menu().click_contents_link()
    assert "Wikipedia:Contents - Wikipedia" in create_driver.title, "Wrong title in contents page link"
    main_page.get_back()

    main_page.click_sidebar_menu().click_current_events_link()
    assert "Portal:Current events - Wikipedia" in create_driver.title, "Wrong title in current events page link"
    main_page.get_back()

    main_page.click_sidebar_menu().click_about_link()
    assert "Wikipedia:About - Wikipedia" in create_driver.title, "Wrong title in about page link"


@pytest.mark.parametrize("create_driver", [ReadConfig.get_base_url()], indirect=True)
def test_main_page_logo(create_driver, main_page):
    assert main_page.is_wiki_logo_icon() == {'x': 92.0, 'y': 8.0, 'width': 50.0, 'height': 50.0}, \
        "Alert! Wrong logo icon position!"
    assert main_page.is_wiki_logo_container() == {'height': 36.0, 'width': 120.0, 'x': 152.0, 'y': 15.0}, \
        "Alert!  Wrong logo container position!"


@pytest.mark.parametrize("create_driver", [ReadConfig.get_base_url()], indirect=True)
def test_main_page_css_value(create_driver, main_page):
    assert main_page.is_css_value_background_color() == "rgb(255, 255, 255)", "Alert! Wrong background-color!"
    assert main_page.is_css_value_font_family() == "sans-serif", "Alert! Wrong font-family!"


@pytest.mark.parametrize("create_driver", [ReadConfig.get_base_url()], indirect=True)
def test_main_page_current_url(create_driver, main_page):
    assert main_page.get_current_url() == "https://en.wikipedia.org/wiki/Main_Page", "Alert! Not main page url!"
    main_page.click_common_page()
    assert main_page.get_current_url() == "https://commons.wikimedia.org/wiki/Main_Page", "Alert! Not commons page url!"
    main_page.get_back()

    main_page.click_wikibooks_page()
    assert main_page.get_current_url() == "https://en.wikibooks.org/wiki/Main_Page", "Alert! Not wikibooks page url!"
    main_page.get_back()

    main_page.click_mediawiki_page()
    assert main_page.get_current_url() == "https://www.mediawiki.org/wiki/MediaWiki", "Alert! Not mediawiki page url!"
