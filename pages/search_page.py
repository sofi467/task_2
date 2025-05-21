from selenium.common import TimeoutException

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re


class SearchPage(BasePage):
    CHECK_PAGE = (By.ID, "search_result_container")
    SORT_BY = (By.ID, "sort_by_trigger")
    FILTER_BY = (By.ID, "Price_DESC")
    LOAD_RESULT = (By.XPATH, "//*[contains(@id, 'search_result_container') and contains(@style, 'opacity')]")
    SEARCH_RESULT = (By.XPATH, "//*[contains(@class,'discount_final_price')]")

    # def is_page_loaded(self):
    #     try:
    #         self.wait.until(EC.visibility_of_element_located(self.PAGE_CHECK))
    #         return True
    #     except TimeoutException:
    #         return False

    def sort_by_price(self):
        sort_by = self.wait.until(EC.element_to_be_clickable(self.SORT_BY))
        sort_by.click()

    def filter_by_trigger(self):
        filter_by = self.wait.until(EC.visibility_of_element_located(self.FILTER_BY))
        filter_by.click()

    def is_display_sorted(self):
        try:
            self.wait.until(EC.invisibility_of_element_located(self.LOAD_RESULT))
            return True
        except TimeoutException:
            return False

    def sort_by_n_position(self, n):
        elements = self.wait.until(EC.visibility_of_all_elements_located(self.SEARCH_RESULT))
        return elements[:n]

    def get_prices_from_elements(self, elements):
        prices = []
        for element in elements:
            text = element.text.replace('руб.', '').strip()
            match = re.search(r'\d+[.,]?\d*', text)
            if match:
                price_str = match.group(0).replace(',', '.')
                price_value = float(price_str)
                prices.append(price_value)

        return prices
