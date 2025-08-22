from playwright.sync_api import expect

class FinishPage:
    def __init__(self, page):
        self.page = page

    def verify_success(self):
        expect(self.page.locator('.complete-header')).to_have_text("Thank you for your order!")
