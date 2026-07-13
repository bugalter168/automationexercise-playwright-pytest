import allure


@allure.feature("Authentication")
@allure.story("Register User")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("TC1: Register a new user end to end and delete the account")
def test_register_user(
    base_url, home_page, login_page, signup_page, account_created_page,
    account_deleted_page, registered_user,
):
    user = registered_user

    home_page.load(base_url)
    home_page.expect_home_page_visible()

    home_page.navbar.go_to_login()
    login_page.expect_new_user_signup_visible()

    login_page.signup(user.name, user.email)

    signup_page.expect_account_information_visible()
    signup_page.fill_account_information(user)
    signup_page.submit_create_account()

    account_created_page.expect_account_created()
    account_created_page.click_continue()

    home_page.navbar.expect_logged_in_as(user.name)

    home_page.navbar.delete_account()
    account_deleted_page.expect_account_deleted()
    account_deleted_page.click_continue()
