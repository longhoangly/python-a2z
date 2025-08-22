import pytest
from playwright.sync_api import Page, expect

def test_saucedemo_login_and_checkout(page):
    page.goto("https://www.saucedemo.com/")

    # Login
    page.fill('input#user-name', 'standard_user')
    page.fill('input#password', 'secret_sauce')
    page.click('input#login-button')

    # Add item to cart
    page.click('button[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click('.shopping_cart_link')

    # Proceed to checkout
    page.click('button[data-test="checkout"]')
    page.fill('input#first-name', 'Long')
    page.fill('input#last-name', 'Ly')
    page.fill('input#postal-code', '70000')
    page.click('input[data-test="continue"]')

    # Final step
    page.click('button[data-test="finish"]')

    # Assertion
    expect(page.locator('.complete-header')).to_have_text("Thank you for your order!")w