from playwright.sync_api import expect


class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def fill_checkout_form(self, first_name, last_name, zip_code):
        self.page.fill("input#first-name", first_name)
        self.page.fill("input#last-name", last_name)
        self.page.fill("input#postal-code", zip_code)
        self.page.click('input[data-test="continue"]')

    def finish_checkout(self):
        self.page.click('button[data-test="finish"]')

    def verify_checkout_success(self):
        expect(self.page.locator(".complete-header")).to_have_text(
            "Thank you for your order!"
        )
