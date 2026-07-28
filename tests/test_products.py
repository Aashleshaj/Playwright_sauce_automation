from playwright.sync_api import Page, expect
from pages.login_sauce_page import LoginPage
from pages.buy_product_page import HomePage

def test_login_validation_blank_fields(page: Page) -> None:
    # 1. Navigate to https://www.saucedemo.com/
    # 2. Leave Username and Password fields empty.
    # 3. Click 'Login'.
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("", "")
    # Expected: Error message 'Epic sadface: Username is required' is displayed.
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Username is required")

def test_add_single_product_to_cart(page: Page) -> None:
    # 1. Log in as 'standard_user'.
    # 2. Click 'Add to cart' for 'Sauce Labs Backpack'.
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    home_page = HomePage(page)
    home_page.add_product_to_cart_by_name("Sauce Labs Backpack")
    
    # Expected: Cart badge count shows '1' and button text changes to 'Remove'.
    expect(home_page.cart_badge).to_have_text("1")
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_be_visible()

def test_add_multiple_products_to_cart(page: Page) -> None:
    # 1. Log in as 'standard_user'.
    # 2. Click 'Add to cart' on 'Sauce Labs Backpack'.
    # 3. Click 'Add to cart' on 'Sauce Labs Bike Light'.
    # 4. Click 'Add to cart' on 'Sauce Labs Bolt T-Shirt'.
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    home_page = HomePage(page)
    home_page.add_product_to_cart_by_name("Sauce Labs Backpack")
    home_page.add_product_to_cart_by_name("Sauce Labs Bike Light")
    home_page.add_product_to_cart_by_name("Sauce Labs Bolt T-Shirt")
    
    # Expected: Cart badge updates to display '3'.
    expect(home_page.cart_badge).to_have_text("3")
