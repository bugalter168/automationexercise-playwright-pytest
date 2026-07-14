from pages.base_page import BasePage


class NavBar(BasePage):
    """Header navigation bar present on every page of the site."""

    def __init__(self, page):
        super().__init__(page)
        header = page.locator("#header")
        # Nav link accessible names are prefixed with a Font Awesome icon glyph
        # (e.g. " Cart"), so `exact=True` never matches; scoping to the
        # unique #header container instead avoids colliding with unrelated
        # same-text links/buttons elsewhere on a given page.
        self.home_link = header.get_by_role("link", name="Home")
        self.products_link = header.get_by_role("link", name="Products")
        self.cart_link = header.get_by_role("link", name="Cart")
        self.signup_login_link = header.get_by_role("link", name="Signup / Login")
        self.logout_link = header.get_by_role("link", name="Logout")
        self.delete_account_link = header.get_by_role("link", name="Delete Account")
        self.test_cases_link = header.get_by_role("link", name="Test Cases")
        self.contact_us_link = header.get_by_role("link", name="Contact us")
        self.logged_in_as_text = header.locator(".nav", has_text="Logged in as")

    def go_to_products(self) -> None:
        self.click(self.products_link, "Products nav link")

    def go_to_cart(self) -> None:
        self.click(self.cart_link, "Cart nav link")

    def go_to_login(self) -> None:
        self.click(self.signup_login_link, "Signup / Login nav link")

    def go_to_test_cases(self) -> None:
        self.click(self.test_cases_link, "Test Cases nav link")

    def go_to_contact_us(self) -> None:
        self.click(self.contact_us_link, "Contact us nav link")

    def logout(self) -> None:
        self.click(self.logout_link, "Logout nav link")

    def delete_account(self) -> None:
        self.click(self.delete_account_link, "Delete Account nav link")

    def expect_logged_in_as(self, username: str, timeout: float | None = None) -> None:
        self.expect_text(
            self.logged_in_as_text, f"Logged in as {username}", "logged-in indicator", timeout=timeout
        )


class SubscriptionWidget(BasePage):
    """Footer subscription form, present on the home and cart pages."""

    def __init__(self, page):
        super().__init__(page)
        self.heading = page.locator("h2", has_text="Subscription")
        self.email_input = page.locator("#susbscribe_email")
        self.subscribe_button = page.locator("#subscribe")
        self.success_message = page.locator("#success-subscribe .alert-success")

    def subscribe(self, email: str) -> None:
        self.scroll_to_bottom()
        self.expect_visible(self.heading, "Subscription heading")
        self.fill(self.email_input, email, "subscription email")
        self.click(self.subscribe_button, "subscribe arrow button")

    def expect_subscribed_successfully(self) -> None:
        self.expect_text(
            self.success_message,
            "You have been successfully subscribed!",
            "subscription success message",
        )


class CategorySidebar(BasePage):
    """Left-hand CATEGORY / BRANDS sidebar shown on the home, products,
    category and brand listing pages."""

    def __init__(self, page):
        super().__init__(page)
        self.sidebar = page.locator(".left-sidebar")
        # Category accordion toggles are anchors with fragment hrefs (#Women …).
        self.women_toggle = self.sidebar.locator('a[href="#Women"]')
        self.men_toggle = self.sidebar.locator('a[href="#Men"]')
        self.kids_toggle = self.sidebar.locator('a[href="#Kids"]')
        self.brand_links = page.locator(".brands_products .nav-pills li a")

    def open_women_category(self) -> None:
        self.click(self.women_toggle, "Women category toggle")

    def open_men_category(self) -> None:
        self.click(self.men_toggle, "Men category toggle")

    def click_category_link(self, name: str) -> None:
        # Subcategory links live in the expanded accordion panel; match by
        # visible text (the anchor's accessible name is just the plain name).
        link = self.sidebar.get_by_role("link", name=name, exact=True)
        self.click(link, f"'{name}' category link")

    def expect_brands_visible(self) -> None:
        self.expect_visible(self.brand_links.first, "brands sidebar")

    def click_brand(self, name: str) -> None:
        # Brand anchors carry a count span (e.g. "(6)Polo"), so target the
        # stable href instead of the accessible name.
        self.click(self.page.locator(f'.brands_products a[href="/brand_products/{name}"]'), f"'{name}' brand link")
