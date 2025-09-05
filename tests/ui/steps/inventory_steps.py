import pytest
import allure

from tests.ui.pages.inventory_page import InventoryPage


@pytest.fixture(scope="function")
def inventory_steps(page):
    return InventorySteps(page)


class InventorySteps:
    def __init__(self, page):
        self.inventory_page = InventoryPage(page)

    @allure.step("add item and open cart")
    def add_item_and_open_cart(self):
        self.inventory_page.add_item_to_cart()
        self.inventory_page.go_to_cart()
