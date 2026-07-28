from playwright.sync_api import Page, expect
from pages.login_sauce_page import LoginPage
from pages.buy_product_page import HomePage

def test_checkout_validation_missing_postal_code(page: Page) -> None:
    # 1. Log in and proceed to Checkout Step One.
    # 2. Enter First Name 'John' and Last Name 'Doe'.
    # 3. Leave Zip/Postal Code blank.
    # 4. Click 'Continue'.
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    home_page = HomePage(page)
    home_page.add_product_to_cart_by_name("Sauce Labs Backpack")
    home_page.go_to_cart()
    home_page.proceed_to_checkout()
    home_page.fill_checkout_info("John", "Doe", "")
    
    # Expected: Error banner displays 'Error: Postal Code is required'.
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Error: Postal Code is required")

def test_cancel_checkout_from_overview(page: Page) -> None:
    # 1. Add item to cart, proceed through Checkout Step One to Checkout Overview.
    # 2. Click 'Cancel'.
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    home_page = HomePage(page)
    home_page.add_product_to_cart_by_name("Sauce Labs Backpack")
    home_page.go_to_cart()
    home_page.proceed_to_checkout()
    home_page.fill_checkout_info("John", "Doe", "12345")
    home_page.cancel_checkout()
    
    # Expected: User is redirected to '/inventory.html' and cart items remain intact.
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(home_page.cart_badge).to_have_text("1")

def test_verify_checkout_price_calculation(page: Page) -> None:
    # 1. Add 'Sauce Labs Backpack' ($29.99) and 'Sauce Labs Bike Light' ($9.99) to cart.
    # 2. Complete Checkout Step One and view Overview page.
    # 3. Verify Item total, Tax, and Total labels.
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    home_page = HomePage(page)
    home_page.add_product_to_cart_by_name("Sauce Labs Backpack")
    home_page.add_product_to_cart_by_name("Sauce Labs Bike Light")
    home_page.go_to_cart()
    home_page.proceed_to_checkout()
    home_page.fill_checkout_info("John", "Doe", "12345")
    
    # Expected: Item total shows '$39.98', Tax shows '$3.20', and Total shows '$43.18'.
    summary = home_page.get_checkout_summary_info()
    assert "39.98" in summary["item_total"]
    assert "3.20" in summary["tax"]
    assert "43.18" in summary["total"]
