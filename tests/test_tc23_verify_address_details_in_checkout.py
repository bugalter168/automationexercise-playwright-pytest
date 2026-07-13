import allure


@allure.feature("Checkout & Orders")
@allure.story("Address Verification")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("TC23: Checkout address matches the address entered at registration")
def test_verify_address_details_in_checkout(
    base_url, home_page, login_page, signup_page, account_created_page,
    cart_page, checkout_page, account_deleted_page, registered_user,
):
    user = registered_user

    home_page.load(base_url)
    home_page.navbar.go_to_login()
    login_page.signup(user.name, user.email)
    signup_page.expect_account_information_visible()
    signup_page.fill_account_information(user)
    signup_page.submit_create_account()

    account_created_page.expect_account_created()
    account_created_page.click_continue()

    home_page.navbar.expect_logged_in_as(user.name)

    home_page.add_product_to_cart_by_index(0)
    home_page.click_continue_shopping()

    home_page.navbar.go_to_cart()
    cart_page.click_proceed_to_checkout()

    checkout_page.expect_address_and_order_review_visible()
    checkout_page.expect_address_matches(
        [
            f"{user.title}. {user.first_name} {user.last_name}",
            user.address1,
            user.address2,
            user.city,
            user.state,
            user.zipcode,
            user.country,
            user.mobile_number,
        ]
    )

    home_page.navbar.delete_account()
    account_deleted_page.expect_account_deleted()
    account_deleted_page.click_continue()
