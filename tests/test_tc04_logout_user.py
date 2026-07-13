import allure


@allure.feature("Authentication")
@allure.story("Logout")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("TC4: Logout returns the user to the login page")
def test_logout_user(base_url, home_page, login_page, existing_user):
    user = existing_user

    home_page.load(base_url)
    home_page.expect_home_page_visible()

    home_page.navbar.go_to_login()
    login_page.expect_login_heading_visible()

    login_page.login(user.email, user.password)
    home_page.navbar.expect_logged_in_as(user.name)

    home_page.navbar.logout()

    login_page.expect_login_heading_visible()
    login_page.expect_url_contains("/login")
