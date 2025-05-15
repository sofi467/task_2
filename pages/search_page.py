from selenium.common import TimeoutException

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re


class SearchPage(BasePage):
    PAGE_CHECK = (By.ID, "search_result_container")
    SORT_BY = (By.ID, "sort_by_trigger")
    FILTER_BY = (By.ID, "Price_DESC")
    SEARCH_RESULT = (By.XPATH, "//*[@class='discount_final_price']")

    def load_page(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.PAGE_CHECK))
            return True
        except TimeoutException:
            return False

    def sort_by_price(self):
        sort_by = self.wait.until(EC.element_to_be_clickable(self.SORT_BY))
        sort_by.click()

    def filter_by_trigger(self):
        filter_by = self.wait.until(EC.element_to_be_clickable(self.FILTER_BY))
        filter_by.click()

    def sort_display(self):
        try:
            self.wait.until(EC.visibility_of_all_elements_located(self.SEARCH_RESULT))
            return True
        except TimeoutException:
            return False

    def sort_n_position(self, n):
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

    def is_sorted_desc(self, prices):
        sorted_prices = sorted(prices, reverse=True)
        if prices != sorted_prices:
            print("Prices not sorted!")
            print("Actual: ", prices)
            print("Expected:", sorted_prices)
            return False
        return True
