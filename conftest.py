import pytest
from selenium import webdriver
from selene.api import browser
from selene import config


@pytest.fixture(scope='session')
def open_base_url(set_browser, set_base_url):
    base_url = set_base_url
    driver = set_browser
    browser.set_driver(driver)
    driver.maximize_window()
    config.timeout = 10
    browser.open_url(base_url)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def set_browser(request):
    driver = request.config.getoption("--browser")
    if driver == 'chrome':
        driver = webdriver.Chrome()
    elif driver == 'firefox':
        driver = webdriver.Firefox(capabilities={"marionette": False},
                                   firefox_binary="C:/Program Files/Mozilla Firefox/firefox.exe")
    elif driver == 'safari':
        driver = webdriver.Safari()
    else:
        driver = webdriver.Ie()
    return driver


@pytest.fixture(scope='session')
def set_base_url(request):
    return request.config.getoption("--base_url")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default='chrome', help="Set browser chrome, firefox, safari or ie")
    parser.addoption("--base_url", action="store", help="Set base url for starting tests")
