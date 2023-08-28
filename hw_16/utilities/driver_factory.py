from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('window-size=1920,1080')
        driver = webdriver.Chrome(options=chrome_options)
        return driver
    else:
        driver = webdriver.Chrome()
        return driver
