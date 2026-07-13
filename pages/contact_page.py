from pages.base_page import BasePage
from pages.components import NavBar


class ContactPage(BasePage):
    URL_PATH = "/contact_us"

    def __init__(self, page):
        super().__init__(page)
        self.navbar = NavBar(page)

        self.get_in_touch_heading = page.locator("h2", has_text="Get In Touch")
        self.name_input = page.locator('input[data-qa="name"]')
        self.email_input = page.locator('input[data-qa="email"]')
        self.subject_input = page.locator('input[data-qa="subject"]')
        self.message_input = page.locator('textarea[data-qa="message"]')
        self.upload_file_input = page.locator('input[name="upload_file"]')
        self.submit_button = page.locator('input[data-qa="submit-button"]')
        self.success_message = page.locator(".status.alert-success")
        self.home_button = page.locator("a.btn-success", has_text="Home")

    def load(self, base_url: str) -> None:
        self.goto(f"{base_url}{self.URL_PATH}")

    def expect_get_in_touch_visible(self) -> None:
        self.expect_visible(self.get_in_touch_heading, "'GET IN TOUCH' heading")

    def fill_form(self, name: str, email: str, subject: str, message: str, file_path: str) -> None:
        self.fill(self.name_input, name, "name")
        self.fill(self.email_input, email, "email")
        self.fill(self.subject_input, subject, "subject")
        self.fill(self.message_input, message, "message")
        self.upload_file(self.upload_file_input, file_path, "attachment")

    def submit(self) -> None:
        # Submitting triggers a native `window.confirm()` ("Press OK to proceed!");
        # accept it so the form actually posts instead of blocking.
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.click(self.submit_button, "Submit button")

    def expect_success_message(self) -> None:
        self.expect_text(
            self.success_message,
            "Success! Your details have been submitted successfully.",
            "form submission success message",
        )

    def click_home(self) -> None:
        self.click(self.home_button, "Home button")
