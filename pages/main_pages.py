from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class MainPages(BasePage):
    CHECK_PAGE = (By.ID, "home_featured_and_recommended")
    SEARCH = (By.ID, "store_nav_search_term")

    def is_page_visibility(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.CHECK_PAGE))
            return True
        except TimeoutException:
            return False

    def search_for_a_game(self, game):
        search_games = self.wait.until(EC.visibility_of_element_located(self.SEARCH))
        search_games.send_keys(game)
        search_games.send_keys(Keys.RETURN)
