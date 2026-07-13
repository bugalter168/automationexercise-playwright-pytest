from pages.base_page import BasePage
from pages.components import NavBar, SubscriptionWidget


class CartPage(BasePage):
    URL_PATH = "/view_cart"

    def __init__(self, page):
        super().__init__(page)
        self.navbar = NavBar(page)
        self.subscription = SubscriptionWidget(page)

        self.cart_rows = page.locator("#cart_info tbody tr")
        # The "Proceed To Checkout" element is an <a> with no href (JS-driven
        # click handler), so it never gets an implicit "link" accessibility
        # role — role-based lookup times out. Target its class instead.
        self.proceed_to_checkout_button = page.locator("a.check_out")
        self.checkout_modal = page.locator("#checkoutModal")
        self.checkout_modal_register_login_link = self.checkout_modal.get_by_role(
            "link", name="Register / Login"
        )
        self.empty_cart_message = page.locator("#empty_cart")

    def load(self, base_url: str) -> None:
        self.goto(f"{base_url}{self.URL_PATH}")

    def row_for_product(self, product_id: int):
        return self.page.locator(f"#product-{product_id}")

    def expect_product_in_cart(self, product_id: int) -> None:
        self.expect_visible(self.row_for_product(product_id), f"cart row for product {product_id}")

    def expect_product_not_in_cart(self, product_id: int) -> None:
        self.expect_hidden(self.row_for_product(product_id), f"cart row for product {product_id}")

    def get_price(self, product_id: int) -> str:
        return self.get_text(self.row_for_product(product_id).locator(".cart_price"))

    def get_quantity(self, product_id: int) -> str:
        return self.get_text(self.row_for_product(product_id).locator(".cart_quantity button"))

    def get_total(self, product_id: int) -> str:
        return self.get_text(self.row_for_product(product_id).locator(".cart_total .cart_total_price"))

    def remove_product(self, product_id: int) -> None:
        self.click(
            self.row_for_product(product_id).locator(".cart_quantity_delete"),
            f"remove ('X') button for product {product_id}",
        )

    def click_proceed_to_checkout(self) -> None:
        self.click(self.proceed_to_checkout_button, "Proceed To Checkout button")

    def expect_checkout_login_prompt_visible(self) -> None:
        self.expect_visible(self.checkout_modal, "Register/Login checkout prompt modal")

    def click_register_login_in_modal(self) -> None:
        self.click(self.checkout_modal_register_login_link, "Register / Login link in checkout modal")
