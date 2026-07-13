from pages.base_page import BasePage
from pages.components import CategorySidebar, NavBar


class ProductsPage(BasePage):
    URL_PATH = "/products"

    def __init__(self, page):
        super().__init__(page)
        self.navbar = NavBar(page)
        self.sidebar = CategorySidebar(page)

        self.page_heading = page.locator(".features_items h2.title")
        self.search_input = page.locator("#search_product")
        self.search_button = page.locator("#submit_search")
        self.product_cards = page.locator(".features_items .product-image-wrapper")

    def load(self, base_url: str) -> None:
        self.goto(f"{base_url}{self.URL_PATH}")

    def expect_all_products_visible(self) -> None:
        self.expect_text(self.page_heading, "All Products", "'ALL PRODUCTS' heading")

    def search_product(self, name: str) -> None:
        self.fill(self.search_input, name, "search product input")
        self.click(self.search_button, "search button")

    def expect_searched_products_visible(self) -> None:
        self.expect_text(self.page_heading, "Searched Products", "'SEARCHED PRODUCTS' heading")

    def expect_products_visible(self) -> None:
        self.expect_visible(self.product_cards.first, "search results grid")

    def product_count(self) -> int:
        return self.product_cards.count()

    def product_id_by_index(self, index: int) -> int:
        add_to_cart = self.product_cards.nth(index).locator(".add-to-cart").first
        return int(add_to_cart.get_attribute("data-product-id"))

    def hover_product_card(self, index: int) -> None:
        self.hover(self.product_cards.nth(index), f"product card #{index + 1}")

    def add_product_to_cart_by_index(self, index: int) -> None:
        card = self.product_cards.nth(index)
        self.hover(card, f"product card #{index + 1}")
        self.click(
            card.locator(".product-overlay .add-to-cart"),
            f"Add to cart on product card #{index + 1}",
        )

    def add_product_to_cart_by_name(self, name: str) -> None:
        card = self.product_cards.filter(has_text=name).first
        self.hover(card, f"product card '{name}'")
        self.click(card.locator(".product-overlay .add-to-cart"), f"Add to cart on '{name}'")

    def view_product_by_index(self, index: int) -> None:
        self.click(
            self.product_cards.nth(index).get_by_role("link", name="View Product"),
            f"View Product link on card #{index + 1}",
        )

    def click_continue_shopping(self) -> None:
        self.click(self.page.locator(".modal.show .close-modal"), "Continue Shopping button")

    def click_view_cart_from_modal(self) -> None:
        self.click(self.page.locator(".modal.show").get_by_role("link", name="View Cart"), "View Cart link in modal")


class CategoryBrandPage(BasePage):
    """The product-listing page shown at /category_products/<id> or /brand_products/<name>."""

    def __init__(self, page):
        super().__init__(page)
        self.navbar = NavBar(page)
        self.sidebar = CategorySidebar(page)
        self.page_heading = page.locator(".features_items h2.title")
        self.product_cards = page.locator(".features_items .product-image-wrapper")

    def expect_heading_contains(self, text: str) -> None:
        self.expect_text(self.page_heading, text, "category/brand page heading")

    def expect_products_visible(self) -> None:
        self.expect_visible(self.product_cards.first, "product listing grid")
