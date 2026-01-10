from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.product_title_link = page.locator("[data-test=\"item-3-title-link\"]")
        self.add_to_cart_button = page.locator("[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]")
        self.shopping_cart_link = page.locator("[data-test=\"shopping-cart-link\"]")

    def verify_product_visible(self) -> None:
        expect(self.product_title_link).to_be_visible()

    def add_product_to_cart(self) -> None:
        self.add_to_cart_button.click()

    def go_to_cart(self) -> None:
        self.shopping_cart_link.click() 

    def checkout(self) -> None:
        self.page.locator("[data-test=\"checkout\"]").click()
        self.page.locator("[data-test=\"firstName\"]").fill("Aashlesha")
        self.page.locator("[data-test=\"lastName\"]").fill("J")
        self.page.locator("[data-test=\"postalCode\"]").fill("ABCV")
        self.page.locator("[data-test=\"continue\"]").click()
        self.page.locator("[data-test=\"finish\"]").click()

    def navigate(self) -> None:
        self.page.goto("https://www.saucedemo.com/")