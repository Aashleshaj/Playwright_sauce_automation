from playwright.sync_api import Page, expect
from pages.login_sauce_page import LoginPage

def test_successful_login(page: Page) -> None:
    # 1. Navigate to https://www.saucedemo.com/
    # 2. Enter 'standard_user' into Username.
    # 3. Enter 'secret_sauce' into Password.
    # 4. Click 'Login'.
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    # Expected: User is redirected to '/inventory.html'
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_locked_out_user(page: Page) -> None:
    # 1. Navigate to https://www.saucedemo.com/
    # 2. Enter 'locked_out_user' into Username.
    # 3. Enter 'secret_sauce' into Password.
    # 4. Click 'Login'.
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")
    # Expected: error banner displays 'Epic sadface: Sorry, this user has been locked out.'
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Sorry, this user has been locked out.")

def test_invalid_password(page: Page) -> None:
    # 1. Navigate to https://www.saucedemo.com/
    # 2. Enter 'standard_user' into Username.
    # 3. Enter 'wrong_password' into Password.
    # 4. Click 'Login'.
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "wrong_password")
    # Expected: Error message 'Epic sadface: Username and password do not match any user in this service' is displayed.
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Username and password do not match any user in this service")
