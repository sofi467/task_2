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
    base_url = config_reader.get_value('base_url')
    url_with_lang = f"{base_url}?l={language}" if language else base_url
    options = Options()
    options.add_argument(f'--lang={language}')
    driver = webdriver.Chrome(options=options)
    driver.get(url_with_lang)
    return driver
