import pytest
from config_reader import ConfigReader
from singleton_wb import WebDriverSingleton


@pytest.fixture(scope="session")
def config_reader():
    return ConfigReader('config.json')


@pytest.fixture(scope="session")
def driver():
    driver = WebDriverSingleton()
    yield driver
    WebDriverSingleton.quit()


@pytest.fixture
def driver_with_url(driver, config_reader, request):
    language = getattr(request, 'param', None)
    base_url = config_reader.get_value('base_url')
    url_with_lang = f"{base_url}?l={language}" if language else base_url
    driver.get(url_with_lang)
    return driver
