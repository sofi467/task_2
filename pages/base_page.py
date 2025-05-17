from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    config_reader = None

    def __init__(self, driver, config_reader):
        self.driver = driver
        self.timeout = config_reader.get_value('timeout')
        self.wait = Wait(driver, self.timeout)

    def wait_for_url_change(self, old_url):
        self.wait.until(EC.url_changes(old_url))
