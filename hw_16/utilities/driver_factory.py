from selenium import webdriver

EDGE = 1
FIREFOX = 2
CHROME = 3


def create_driver_factory(driver_id):
    if int(driver_id) == EDGE:
        driver = webdriver.Edge()
        return driver
    elif int(driver_id) == FIREFOX:
        driver = webdriver.Firefox()
        return driver
    elif int(driver_id) == CHROME:
        driver = webdriver.Chrome()
        return driver
    else:
        driver = webdriver.Chrome()
        return driver
