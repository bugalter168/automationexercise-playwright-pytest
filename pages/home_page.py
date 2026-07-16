from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.components import CategorySidebar, NavBar, SubscriptionWidget


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar = NavBar(page)
        self.subscription = SubscriptionWidget(page)
        self.sidebar = CategorySidebar(page)
        self.hero_text = page.get_by_text(
            "Full-Fledged practice website for Automation Engineers"
        ).first
        self.scroll_up_button = page.locator("#scrollUp")
        self.product_cards = page.locator(".features_items .product-image-wrapper")
        self.recommended_items_heading = page.locator(
            ".recommended_items h2", has_text="recommended items"
        )
        self.recommended_add_to_cart = page.locator(
            ".recommended_items .add-to-cart"
        )

    def load(self, base_url: str) -> None:
        self.goto(base_url)

    def expect_home_page_visible(self, timeout: float | None = None) -> None:
        self.expect_visible(self.hero_text, "home page hero text", timeout=timeout)

    def hover_product_card(self, index: int) -> None:
        self.hover(self.product_cards.nth(index), f"product card #{index + 1}")

    def add_product_to_cart_by_index(self, index: int) -> None:
        card = self.product_cards.nth(index)
        self.hover(card, f"product card #{index + 1}")
        self.click(
            card.locator(".product-overlay .add-to-cart"),
            f"Add to cart on product card #{index + 1}",
        )

    def view_product_by_index(self, index: int) -> None:
        self.click(
            self.product_cards.nth(index).get_by_role("link", name="View Product"),
            f"View Product link on card #{index + 1}",
        )

    def click_continue_shopping(self) -> None:
        self.click(self.page.locator(".modal.show .close-modal"), "Continue Shopping button")

    def click_view_cart_from_modal(self) -> None:
        self.click(self.page.locator(".modal.show").get_by_role("link", name="View Cart"), "View Cart link in modal")

    def recommended_item_id(self, index: int = 0) -> int:
        return int(self.recommended_add_to_cart.nth(index).get_attribute("data-product-id"))

    def add_recommended_item_to_cart(self, index: int = 0) -> None:
        self.scroll_to_bottom()
        self.expect_visible(self.recommended_items_heading, "Recommended items heading")
        self.click(self.recommended_add_to_cart.nth(index), "Add To Cart on recommended item")

    def scroll_up_via_arrow(self) -> None:
        self.click(self.scroll_up_button, "scroll-up arrow button")
        self.page.wait_for_timeout(500)
