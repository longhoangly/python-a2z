import pytest
import allure

from tests.ui.pages.cart_page import CartPage


@pytest.fixture(scope="function")
def cart_steps(page):
    return CartSteps(page)


class CartSteps:
    def __init__(self, page):
        self.cart_page = CartPage(page)

    @allure.step("navigate to checkout page")
    def go_checkout(self):
        self.cart_page.click_checkout()
