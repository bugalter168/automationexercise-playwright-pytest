import os
import re

import allure
import pytest
from dotenv import load_dotenv

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.contact_page import ContactPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.payment_page import OrderPlacedPage, PaymentPage
from pages.product_detail_page import ProductDetailPage
from pages.products_page import CategoryBrandPage, ProductsPage
from pages.signup_page import AccountCreatedPage, AccountDeletedPage, SignupPage
from pages.test_cases_page import TestCasesPage
from utils.api_client import delete_account
from utils.data_generator import UserData, generate_user

load_dotenv()

AD_DOMAIN_PATTERN = re.compile(
    r"(googlesyndication|doubleclick|adservice\.google|googletagservices|"
    r"amazon-adsystem|google_vignette|pagead2)"
)


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL", "https://www.automationexercise.com").rstrip("/")


@pytest.fixture
def browser_context_args(browser_context_args):
    # accept_downloads defaults to True in Playwright, but WebKit's download
    # handling is more timing-sensitive than Chromium/Firefox (see
    # OrderPlacedPage.download_invoice), so set it explicitly rather than
    # relying on the implicit default.
    return {
        **browser_context_args,
        "viewport": {"width": 1440, "height": 900},
        "accept_downloads": True,
    }


@pytest.fixture(autouse=True)
def block_ad_requests(page):
    """Abort ad-network requests so ad iframes never render and intercept clicks."""
    page.route(AD_DOMAIN_PATTERN, lambda route: route.abort())
    yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page is not None:
            try:
                allure.attach(
                    page.screenshot(full_page=True),
                    name="failure-screenshot",
                    attachment_type=allure.attachment_type.PNG,
                )
            except Exception:
                pass


@pytest.fixture
def new_user_data() -> UserData:
    return generate_user()


@pytest.fixture
def registered_user(base_url):
    """Yields Faker-generated user data; guarantees account cleanup via the API
    even if a test fails before reaching its own UI 'Delete Account' step."""
    user = generate_user()
    yield user
    delete_account(base_url, user.email, user.password)


@pytest.fixture
def sample_upload_file():
    return os.path.join(os.path.dirname(__file__), "data", "sample_upload.txt")


# ---- Page object fixtures -------------------------------------------------


@pytest.fixture
def home_page(page):
    return HomePage(page)


@pytest.fixture
def existing_user(base_url, home_page, login_page, signup_page, account_created_page):
    """Registers a fresh account via the UI, logs it back out, and hands the
    credentials to a test that needs to log in against a *pre-existing* user
    (TC2, TC4, TC16, TC20). Cleans up via the API in teardown."""
    user = generate_user()
    home_page.load(base_url)
    home_page.navbar.go_to_login()
    login_page.signup(user.name, user.email)
    signup_page.fill_account_information(user)
    signup_page.submit_create_account()
    account_created_page.click_continue()
    # Confirm the session is actually logged in before clicking Logout — under
    # CI's parallel/cross-browser load the header can take longer than usual
    # to re-render post-signup, and clicking Logout before it appears is what
    # produced the flaky "waiting for ... Logout" timeout on CI.
    home_page.navbar.expect_logged_in_as(user.name, timeout=15000)
    home_page.navbar.logout()
    home_page.load(base_url)
    yield user
    delete_account(base_url, user.email, user.password)


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def signup_page(page):
    return SignupPage(page)


@pytest.fixture
def account_created_page(page):
    return AccountCreatedPage(page)


@pytest.fixture
def account_deleted_page(page):
    return AccountDeletedPage(page)


@pytest.fixture
def products_page(page):
    return ProductsPage(page)


@pytest.fixture
def category_brand_page(page):
    return CategoryBrandPage(page)


@pytest.fixture
def product_detail_page(page):
    return ProductDetailPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)


@pytest.fixture
def payment_page(page):
    return PaymentPage(page)


@pytest.fixture
def order_placed_page(page):
    return OrderPlacedPage(page)


@pytest.fixture
def contact_page(page):
    return ContactPage(page)


@pytest.fixture
def test_cases_page(page):
    return TestCasesPage(page)
