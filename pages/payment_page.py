from urllib.parse import urljoin

from playwright.sync_api import APIResponse, Page

from pages.base_page import BasePage
from pages.components import NavBar
from utils.constants import CARD_CVC, CARD_EXPIRY_MONTH, CARD_EXPIRY_YEAR, CARD_NUMBER


class PaymentPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.name_on_card_input = page.locator('input[name="name_on_card"]')
        self.card_number_input = page.locator('input[name="card_number"]')
        self.cvc_input = page.locator('input[name="cvc"]')
        self.expiry_month_input = page.locator('input[name="expiry_month"]')
        self.expiry_year_input = page.locator('input[name="expiry_year"]')
        self.pay_button = page.locator('[data-qa="pay-button"]')

    def pay_with_test_card(self, name_on_card: str) -> None:
        self.fill(self.name_on_card_input, name_on_card, "name on card")
        self.fill(self.card_number_input, CARD_NUMBER, "card number")
        self.fill(self.cvc_input, CARD_CVC, "CVC")
        self.fill(self.expiry_month_input, CARD_EXPIRY_MONTH, "expiry month")
        self.fill(self.expiry_year_input, CARD_EXPIRY_YEAR, "expiry year")
        self.click(self.pay_button, "Pay and Confirm Order button")


class OrderPlacedPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar = NavBar(page)
        self.success_heading = page.locator('[data-qa="order-placed"]')
        self.confirmation_text = page.get_by_text("Your order has been confirmed!")
        self.download_invoice_link = page.get_by_role("link", name="Download Invoice")
        self.continue_button = page.locator('[data-qa="continue-button"]')

    def expect_order_placed_success(self) -> None:
        self.expect_visible(self.success_heading, "'ORDER PLACED!' heading")
        self.expect_visible(self.confirmation_text, "order confirmation message")

    def download_invoice(self) -> APIResponse:
        # Fetch the invoice with a direct HTTP request inside the browser's own
        # session (same cookies/auth) instead of catching the browser
        # "download" event, which fires slowly and unreliably on WebKit. The
        # file comes back immediately and identically on all three browsers.
        href = self.download_invoice_link.get_attribute("href")
        url = urljoin(self.page.url, href)
        response = self.page.request.get(url)
        assert response.ok, f"invoice download failed: HTTP {response.status}"
        return response

    def click_continue(self) -> None:
        self.click(self.continue_button, "Continue button")
