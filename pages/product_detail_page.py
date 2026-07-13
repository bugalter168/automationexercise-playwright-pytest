from pages.base_page import BasePage
from pages.components import NavBar


class ProductDetailPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.navbar = NavBar(page)

        self.product_name = page.locator(".product-information h2")
        self.product_price = page.locator(".product-information span span")
        self.category_text = page.locator(".product-information p").filter(has_text="Category:")
        self.availability_text = page.locator(".product-information p").filter(has_text="Availability:")
        self.condition_text = page.locator(".product-information p").filter(has_text="Condition:")
        self.brand_text = page.locator(".product-information p").filter(has_text="Brand:")

        self.quantity_input = page.locator("#quantity")
        self.add_to_cart_button = page.locator(".product-information .cart")

        self.review_name_input = page.locator("#name")
        self.review_email_input = page.locator("#email")
        self.review_text_input = page.locator("#review")
        self.review_submit_button = page.locator("#button-review")
        self.write_review_heading = page.get_by_role("link", name="Write Your Review")
        self.review_success_message = page.locator("#review-form .alert-success")

        self.recommended_items_heading = page.locator(
            ".recommended_items h2", has_text="recommended items"
        )
        self.recommended_add_to_cart = page.locator(".recommended_items .add-to-cart")

    def load(self, base_url: str, product_id: int) -> None:
        self.goto(f"{base_url}/product_details/{product_id}")

    def expect_product_details_visible(self) -> None:
        self.expect_visible(self.product_name, "product name")
        self.expect_visible(self.category_text, "product category")
        self.expect_visible(self.product_price, "product price")
        self.expect_visible(self.availability_text, "product availability")
        self.expect_visible(self.condition_text, "product condition")
        self.expect_visible(self.brand_text, "product brand")

    def set_quantity(self, quantity: int) -> None:
        with_text = str(quantity)
        self.quantity_input.fill(with_text)

    def add_to_cart(self) -> None:
        self.click(self.add_to_cart_button, "Add to cart button")

    def click_view_cart_from_modal(self) -> None:
        self.click(self.page.locator(".modal.show").get_by_role("link", name="View Cart"), "View Cart link in modal")

    def click_continue_shopping(self) -> None:
        self.click(self.page.locator(".modal.show .close-modal"), "Continue Shopping button")

    def submit_review(self, name: str, email: str, review: str) -> None:
        self.fill(self.review_name_input, name, "reviewer name")
        self.fill(self.review_email_input, email, "reviewer email")
        self.fill(self.review_text_input, review, "review text")
        self.click(self.review_submit_button, "review Submit button")

    def expect_review_success(self) -> None:
        self.expect_text(self.review_success_message, "Thank you for your review.", "review success message")

    def add_recommended_item_to_cart(self, index: int = 0) -> None:
        self.scroll_to_bottom()
        self.expect_visible(self.recommended_items_heading, "Recommended items heading")
        self.click(self.recommended_add_to_cart.nth(index), "Add To Cart on recommended item")
