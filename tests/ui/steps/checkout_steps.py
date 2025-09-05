import pytest
import allure

from tests.ui.pages.checkout_page import CheckoutPage


@pytest.fixture(scope="function")
def checkout_steps(page):
    return CheckoutSteps(page)


class CheckoutSteps:
    def __init__(self, page):
        self.checkout_page = CheckoutPage(page)

    @allure.step("proceed checkout and verify")
    def complete_order(self):
        self.checkout_page.fill_checkout_form("Long", "Ly", "70000")
        self.checkout_page.finish_checkout()
        self.checkout_page.verify_checkout_success()
