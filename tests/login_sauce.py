import re
from playwright.sync_api import Page
from pages.login_sauce_page import LoginPage
from pages.buy_product_page import HomePage 

# test example definition
def test_example(page: Page) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    # Check if inventory list is visible instead of non-existent method
    home_page.page.wait_for_selector("[data-test=\"inventory-list\"]")
    home_page.add_product_to_cart_by_name("Sauce Labs Backpack")
    home_page.go_to_cart()
    home_page.proceed_to_checkout()

