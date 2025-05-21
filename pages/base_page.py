from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    config_reader = None

    def __init__(self, driver, config_reader):
        self.driver = driver
        self.timeout = config_reader.get_value('timeout')
        self.wait = Wait(driver, self.timeout)

    def is_load_page(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.CHECK_PAGE))
            return True
        except TimeoutException:
            return False
