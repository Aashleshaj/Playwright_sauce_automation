from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.cart_badge = page.locator("[data-test=\"shopping-cart-badge\"]")
        self.shopping_cart_link = page.locator("[data-test=\"shopping-cart-link\"]")

    def get_cart_badge_count(self) -> str:
        return self.cart_badge.inner_text()

    def add_product_to_cart_by_name(self, product_name: str) -> None:
        # Convert product name to data-test ID format (Sauce Labs Backpack -> sauce-labs-backpack)
        data_test = f"add-to-cart-{product_name.lower().replace(' ', '-')}"
        self.page.locator(f"[data-test=\"{data_test}\"]").click()

    def remove_product_from_cart_by_name(self, product_name: str) -> None:
        # Convert product name to data-test ID format (Sauce Labs Backpack -> sauce-labs-backpack)
        data_test = f"remove-{product_name.lower().replace(' ', '-')}"
        self.page.locator(f"[data-test=\"{data_test}\"]").click()

    def go_to_cart(self) -> None:
        self.shopping_cart_link.click()

    def proceed_to_checkout(self) -> None:
        self.page.locator("[data-test=\"checkout\"]").click()

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.page.locator("[data-test=\"firstName\"]").fill(first_name)
        self.page.locator("[data-test=\"lastName\"]").fill(last_name)
        self.page.locator("[data-test=\"postalCode\"]").fill(postal_code)
        self.page.locator("[data-test=\"continue\"]").click()

    def finish_order(self) -> None:
        self.page.locator("[data-test=\"finish\"]").click()

    def cancel_checkout(self) -> None:
        self.page.locator("[data-test=\"cancel\"]").click()

    def get_checkout_summary_info(self) -> dict:
        return {
            "item_total": self.page.locator("[data-test=\"subtotal-label\"]").inner_text(),
            "tax": self.page.locator("[data-test=\"tax-label\"]").inner_text(),
            "total": self.page.locator("[data-test=\"total-label\"]").inner_text()
        }
