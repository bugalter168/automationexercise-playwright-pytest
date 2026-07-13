import allure

from utils.data_generator import unique_email


@allure.feature("Authentication")
@allure.story("Login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("TC3: Login with an incorrect email and password is rejected")
def test_login_invalid_credentials(base_url, home_page, login_page):
    home_page.load(base_url)
    home_page.expect_home_page_visible()

    home_page.navbar.go_to_login()
    login_page.expect_login_heading_visible()

    login_page.login(unique_email("nouser"), "WrongPassword123!")

    login_page.expect_login_error_visible()
