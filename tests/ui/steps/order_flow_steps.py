from tests.ui.pages.login_page import LoginPage
from tests.ui.pages.inventory_page import InventoryPage
from tests.ui.pages.cart_page import CartPage
from tests.ui.pages.checkout_page import CheckoutPage
from tests.ui.pages.finish_page import FinishPage
import allure


class OrderFlowSteps:
    def __init__(self, page):
        self.page = page
        self.login_page = LoginPage(page)
        self.inventory_page = InventoryPage(page)
        self.cart_page = CartPage(page)
        self.checkout_page = CheckoutPage(page)
        self.finish_page = FinishPage(page)

    @allure.step("Login, shopping and checkout...")
    def complete_order(self):
        self.login_page.load()
        self.login_page.login("standard_user", "secret_sauce")
        self.inventory_page.add_item_to_cart()
        self.inventory_page.go_to_cart()
        self.cart_page.click_checkout()
        self.checkout_page.fill_checkout_form("Long", "Ly", "70000")
        self.checkout_page.finish_checkout()
        self.finish_page.verify_success()
