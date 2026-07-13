from pages.base_page import BasePage
from utils.data_generator import UserData


class SignupPage(BasePage):
    """The 'ENTER ACCOUNT INFORMATION' page shown at /signup after Signup is submitted."""

    def __init__(self, page):
        super().__init__(page)
        self.account_info_heading = page.locator("h2", has_text="Enter Account Information")

        self.title_mr_radio = page.locator("#id_gender1")
        self.title_mrs_radio = page.locator("#id_gender2")
        self.password_input = page.locator("#password")
        self.days_select = page.locator("#days")
        self.months_select = page.locator("#months")
        self.years_select = page.locator("#years")
        self.newsletter_checkbox = page.locator("#newsletter")
        self.optin_checkbox = page.locator("#optin")

        self.first_name_input = page.locator("#first_name")
        self.last_name_input = page.locator("#last_name")
        self.company_input = page.locator("#company")
        self.address1_input = page.locator("#address1")
        self.address2_input = page.locator("#address2")
        self.country_select = page.locator("#country")
        self.state_input = page.locator("#state")
        self.city_input = page.locator("#city")
        self.zipcode_input = page.locator("#zipcode")
        self.mobile_number_input = page.locator("#mobile_number")

        self.create_account_button = page.locator('button[data-qa="create-account"]')

    def expect_account_information_visible(self) -> None:
        self.expect_visible(self.account_info_heading, "'ENTER ACCOUNT INFORMATION' heading")

    def fill_account_information(self, user: UserData) -> None:
        title_radio = self.title_mr_radio if user.title == "Mr" else self.title_mrs_radio
        self.check(title_radio, f"title '{user.title}'")
        self.fill(self.password_input, user.password, "password")
        self.select_option(self.days_select, user.day, "date of birth - day")
        self.select_option(self.months_select, user.month, "date of birth - month")
        self.select_option(self.years_select, user.year, "date of birth - year")
        self.check(self.newsletter_checkbox, "'Sign up for our newsletter!' checkbox")
        self.check(self.optin_checkbox, "'Receive special offers from our partners!' checkbox")

        self.fill(self.first_name_input, user.first_name, "first name")
        self.fill(self.last_name_input, user.last_name, "last name")
        self.fill(self.company_input, user.company, "company")
        self.fill(self.address1_input, user.address1, "address")
        self.fill(self.address2_input, user.address2, "address2")
        self.select_option(self.country_select, user.country, "country")
        self.fill(self.state_input, user.state, "state")
        self.fill(self.city_input, user.city, "city")
        self.fill(self.zipcode_input, user.zipcode, "zipcode")
        self.fill(self.mobile_number_input, user.mobile_number, "mobile number")

    def submit_create_account(self) -> None:
        self.click(self.create_account_button, "Create Account button")


class AccountCreatedPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.heading = page.locator('[data-qa="account-created"]')
        self.continue_button = page.locator('[data-qa="continue-button"]')

    def expect_account_created(self) -> None:
        self.expect_visible(self.heading, "'ACCOUNT CREATED!' message")

    def click_continue(self) -> None:
        self.click(self.continue_button, "Continue button")


class AccountDeletedPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.heading = page.locator('[data-qa="account-deleted"]')
        self.continue_button = page.locator('[data-qa="continue-button"]')

    def expect_account_deleted(self) -> None:
        self.expect_visible(self.heading, "'ACCOUNT DELETED!' message")

    def click_continue(self) -> None:
        self.click(self.continue_button, "Continue button")
