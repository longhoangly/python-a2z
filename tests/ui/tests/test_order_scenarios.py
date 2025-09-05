import allure


@allure.feature("UI Tests")
@allure.story("Login and shopping")
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo_order_flow(login_steps, inventory_steps, cart_steps, checkout_steps):
    login_steps.login("standard_user", "secret_sauce")
    inventory_steps.add_item_and_open_cart()
    cart_steps.go_checkout()
    checkout_steps.complete_order()
