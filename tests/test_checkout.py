from playwright.sync_api import Page, expect
from pages.login_sauce_page import LoginPage
from pages.buy_product_page import HomePage

def test_remove_product_from_cart(page: Page) -> None:
    # 1. Log in and add 'Sauce Labs Backpack' to cart.
    # 2. Click Shopping Cart icon to navigate to '/cart.html'.
    # 3. Click 'Remove' next to 'Sauce Labs Backpack'.
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    home_page = HomePage(page)
    home_page.add_product_to_cart_by_name("Sauce Labs Backpack")
    home_page.go_to_cart()
    home_page.remove_product_from_cart_by_name("Sauce Labs Backpack")
    
    # Expected: Item is removed from list and cart badge is cleared.
    expect(page.locator("[data-test=\"inventory-item-name\"]")).not_to_be_visible()
    expect(home_page.cart_badge).not_to_be_visible()

def test_successful_checkout_flow(page: Page) -> None:
    # 1. Log in as 'standard_user'.
    # 2. Add 'Sauce Labs Backpack' to cart and open cart.
    # 3. Click 'Checkout'.
    # 4. Enter First Name 'John', Last Name 'Doe', Zip '12345', and click 'Continue'.
    # 5. On Overview page, click 'Finish'.
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    home_page = HomePage(page)
    home_page.add_product_to_cart_by_name("Sauce Labs Backpack")
    home_page.go_to_cart()
    home_page.proceed_to_checkout()
    home_page.fill_checkout_info("John", "Doe", "12345")
    home_page.finish_order()
    
    # Expected: Navigated to '/checkout-complete.html' displaying header 'Thank you for your order!'
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(page.locator("[data-test=\"complete-header\"]")).to_have_text("Thank you for your order!")

def test_checkout_validation_missing_first_name(page: Page) -> None:
    # 1. Log in and proceed to Checkout Step One ('/checkout-step-one.html').
    # 2. Leave First Name blank.
    # 3. Enter Last Name 'Doe' and Zip '12345'.
    # 4. Click 'Continue'.
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    home_page = HomePage(page)
    home_page.add_product_to_cart_by_name("Sauce Labs Backpack")
    home_page.go_to_cart()
    home_page.proceed_to_checkout()
    home_page.fill_checkout_info("", "Doe", "12345")
    
    # Expected: Error banner displays 'Error: First Name is required' and user remains on Step One page.
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Error: First Name is required")
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
