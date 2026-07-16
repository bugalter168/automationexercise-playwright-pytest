from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.components import NavBar


class CheckoutPage(BasePage):
    URL_PATH = "/checkout"

    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar = NavBar(page)

        self.address_details_heading = page.locator("h2", has_text="Address Details")
        self.review_order_heading = page.locator("h2", has_text="Review Your Order")
        self.delivery_address = page.locator("#address_delivery")
        self.billing_address = page.locator("#address_invoice")
        self.comment_textarea = page.locator('textarea[name="message"]')
        self.place_order_button = page.get_by_role("link", name="Place Order")

    def expect_address_and_order_review_visible(self) -> None:
        self.expect_visible(self.address_details_heading, "Address Details heading")
        self.expect_visible(self.review_order_heading, "Review Your Order heading")
        self.expect_visible(self.delivery_address, "delivery address block")
        self.expect_visible(self.billing_address, "billing address block")

    def expect_address_matches(self, expected_lines: list[str]) -> None:
        for line in expected_lines:
            self.expect_text(self.delivery_address, line, "delivery address")
            self.expect_text(self.billing_address, line, "billing address")

    def enter_comment(self, comment: str) -> None:
        self.fill(self.comment_textarea, comment, "order comment")

    def place_order(self) -> None:
        self.click(self.place_order_button, "Place Order button")
