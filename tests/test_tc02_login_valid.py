import allure


@allure.feature("Authentication")
@allure.story("Login")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("TC2: Login with a correct email and password")
def test_login_valid_credentials(
    base_url, home_page, login_page, account_deleted_page, existing_user,
):
    user = existing_user

    home_page.load(base_url)
    home_page.expect_home_page_visible()

    home_page.navbar.go_to_login()
    login_page.expect_login_heading_visible()

    login_page.login(user.email, user.password)

    home_page.navbar.expect_logged_in_as(user.name)

    home_page.navbar.delete_account()
    account_deleted_page.expect_account_deleted()
