import pytest


@pytest.mark.parametrize("create_driver", ["env.base_url"], indirect=True)
def test_search_option(create_driver, search_page, env):
    ruscism, selenium, ukraine, sheva = env.search_ruscism, env.search_selenium, env.search_ukraine, env.search_sheva

    search_page.set_searching_data(ruscism).click_search_button_main()
    assert "Ruscism - Wikipedia" in create_driver.title, "Alert! Ruscism not in the title!"
    search_page.set_searching_data(selenium).click_search_button_main().click_on_lang_checkbox().choose_deutsch_lang()
    assert "Selen – Wikipedia" in create_driver.title, "Alert! Selen not in the title!"
    search_page.set_searching_data(ukraine).click_search_button_de_ua().choose_ukrainian_lang()
    assert "Україна — Вікіпедія" in create_driver.title, "Alert! Україна not in the title!"
    search_page.choose_italiano_lang().set_searching_data(sheva).click_search_button_de_ua()
    assert "Andrij Ševčenko - Wikipedia" in create_driver.title, "Alert! Andrij Ševčenko not in the title!"


@pytest.mark.parametrize("create_driver", ["env.base_url"], indirect=True)
def test_search_option_via_invalid_request(create_driver, search_page, env):
    invalid_request = env.invalid_request

    search_page.set_searching_data(invalid_request).click_search_button_main()

    assert search_page.is_request_not_found() == "There were no results matching the query.", \
        "Alert! Wrong answer for request"


@pytest.mark.parametrize("create_driver", ["env.base_url"], indirect=True)
def test_search_option_parametrise_request(create_driver, search_page, env):
    search_request, search_supplement = env.search_swiss, env.search_swiss_supplement

    (search_page.set_searching_data(search_request).click_search_button_main().click_advanced_search_list().
     set_supplement_data(search_supplement).click_search_button())

    assert search_page.is_request_found() == 'There is a page named "Cantons of Switzerland" on Wikipedia', \
        "Alert! Request is not Cantons of Switzerland"


@pytest.mark.parametrize("create_driver", ["env.base_url"], indirect=True)
def test_search_option_empty_request(create_driver, search_page):
    search_page.set_searching_data("").click_search_button_main()

    assert search_page.is_value_empty() == "", "Alert! Value is not ''"


@pytest.mark.parametrize("create_driver", ["env.base_url"], indirect=True)
def test_search_option_request_by_cyrillic(create_driver, search_page, env):
    search_request = env.search_cyrillic

    search_page.set_searching_data(search_request).click_search_button_main()

    assert search_page.is_title_correct() == "Ukraine", "Alert! Title is not Ukraine"
