class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def fill_checkout_form(self, first_name, last_name, zip_code):
        self.page.fill('input#first-name', first_name)
        self.page.fill('input#last-name', last_name)
        self.page.fill('input#postal-code', zip_code)
        self.page.click('input[data-test="continue"]')

    def finish_checkout(self):
        self.page.click('button[data-test="finish"]')