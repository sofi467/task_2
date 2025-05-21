import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config_reader import ConfigReader
from singleton_wb import WebDriverSingleton


@pytest.fixture(scope="session")
def config_reader():
    return ConfigReader()


@pytest.fixture(scope="session")
def driver():
    driver = WebDriverSingleton()
    yield driver
    WebDriverSingleton.quit()


@pytest.fixture(params=["ru", "en"])
def driver_with_url(driver, config_reader, request):
    language = request.param
    options = Options()
    options.add_argument(f'--lang={language}')
    driver = webdriver.Chrome(options=options)
    driver.get(config_reader.get_value('base_url'))
    return driver
