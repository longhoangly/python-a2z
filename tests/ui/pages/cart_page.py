from utils.page_helper import screenshot


class CartPage:
    def __init__(self, page):
        self.page = page

    @screenshot
    def click_checkout(self):
        print("going to click checkout")
        self.page.click('button[data-test="checkout"]')
