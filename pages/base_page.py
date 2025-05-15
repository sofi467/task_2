from selenium.webdriver.support.ui import WebDriverWait as Wait


class BasePage:
    def __init__(self, driver, config_reader):
        self.driver = driver
        self.config_reader = config_reader
        self.timeout = config_reader.get_value('timeout')
        self.wait = Wait(driver, self.timeout)
