from utils.page_helper import screenshots


class CartPage:
    def __init__(self, page):
        self.page = page

    @screenshots
    def click_checkout(self):
        self.page.click('button[data-test="checkout"]')
