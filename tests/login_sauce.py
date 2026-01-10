import re
from playwright.sync_api import Page
from pages.login_sauce_page import LoginPage
from pages.buy_product_page import HomePage 



def test_example(page: Page) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    home_page.verify_product_visible()
    home_page.add_product_to_cart()
    home_page.go_to_cart()
    home_page.checkout()
    home_page.navigate()

