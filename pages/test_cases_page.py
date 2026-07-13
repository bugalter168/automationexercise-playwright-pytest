from pages.base_page import BasePage
from pages.components import NavBar


class TestCasesPage(BasePage):
    URL_PATH = "/test_cases"

    def __init__(self, page):
        super().__init__(page)
        self.navbar = NavBar(page)
        self.page_heading = page.locator("h2", has_text="Test Cases")

    def expect_test_cases_page_visible(self) -> None:
        self.expect_url_contains(self.URL_PATH)
        self.expect_visible(self.page_heading, "'TEST CASES' heading")
