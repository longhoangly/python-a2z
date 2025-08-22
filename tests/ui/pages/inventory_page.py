class InventoryPage:
    def __init__(self, page):
        self.page = page

    def add_item_to_cart(self, item_name="sauce-labs-backpack"):
        self.page.click(f'button[data-test="add-to-cart-{item_name}"]')

    def go_to_cart(self):
        self.page.click('.shopping_cart_link')