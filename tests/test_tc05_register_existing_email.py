import allure


@allure.feature("Authentication")
@allure.story("Register User")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("TC5: Registering with an already-used email is rejected")
def test_register_existing_email(base_url, home_page, login_page, existing_user):
    user = existing_user

    home_page.load(base_url)
    home_page.expect_home_page_visible()

    home_page.navbar.go_to_login()
    login_page.expect_new_user_signup_visible()

    login_page.signup("Another Name", user.email)

    login_page.expect_signup_email_exists_error()
