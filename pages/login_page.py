from pages.base_page import BasePage
from pages.components import NavBar


class LoginPage(BasePage):
    URL_PATH = "/login"

    def __init__(self, page):
        super().__init__(page)
        self.navbar = NavBar(page)

        self.new_user_signup_heading = page.locator(".signup-form h2", has_text="New User Signup!")
        self.signup_name_input = page.locator('input[data-qa="signup-name"]')
        self.signup_email_input = page.locator('input[data-qa="signup-email"]')
        self.signup_button = page.locator('button[data-qa="signup-button"]')
        self.signup_error = page.locator(".signup-form form p", has_text="Email Address already exist!")

        self.login_heading = page.locator(".login-form h2", has_text="Login to your account")
        self.login_email_input = page.locator('input[data-qa="login-email"]')
        self.login_password_input = page.locator('input[data-qa="login-password"]')
        self.login_button = page.locator('button[data-qa="login-button"]')
        self.login_error = page.locator(".login-form form p", has_text="Your email or password is incorrect!")

    def load(self, base_url: str) -> None:
        self.goto(f"{base_url}{self.URL_PATH}")

    def expect_new_user_signup_visible(self) -> None:
        self.expect_visible(self.new_user_signup_heading, "'New User Signup!' heading")

    def expect_login_heading_visible(self) -> None:
        self.expect_visible(self.login_heading, "'Login to your account' heading")

    def signup(self, name: str, email: str) -> None:
        self.fill(self.signup_name_input, name, "signup name")
        self.fill(self.signup_email_input, email, "signup email")
        self.click(self.signup_button, "Signup button")

    def expect_signup_email_exists_error(self) -> None:
        self.expect_visible(self.signup_error, "'Email Address already exist!' error")

    def login(self, email: str, password: str) -> None:
        self.fill(self.login_email_input, email, "login email")
        self.fill(self.login_password_input, password, "login password")
        self.click(self.login_button, "Login button")

    def expect_login_error_visible(self) -> None:
        self.expect_visible(self.login_error, "'Your email or password is incorrect!' error")
