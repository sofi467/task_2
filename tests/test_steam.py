import time

import pytest

from pages.main_pages import MainPages
from pages.search_page import SearchPage


@pytest.mark.parametrize('driver_with_url', ['russian', 'english'], indirect=True)
@pytest.mark.parametrize("game, n", [
    ("The Witcher", 10),
    ("Fallout", 20)
])
class TestSearhGame:
    def test_search_game(self, driver, config_reader, driver_with_url, game, n):
        driver = driver_with_url
        main_page = MainPages(driver, config_reader)
        search_page = SearchPage(driver, config_reader)
        assert main_page.check_is_visibility_page(), "page is not loaded"
        main_page.search_game(game)
        assert search_page.load_page(), "page not loaded"
        search_page.sort_by_price()

        search_page.filter_by_trigger()
        time.sleep(5)

        assert search_page.sort_display(), "sorting not displayed"
        elements = search_page.sort_n_position(n)
        prices = search_page.get_prices_from_elements(elements)

        assert len(prices) == n, f"Получено {len(prices)} цен, ожидалось {n}"
        assert search_page.is_sorted_desc(prices), f"Цены не отсортированы по убыванию: {prices}"
