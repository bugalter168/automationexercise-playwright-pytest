import allure


@allure.feature("Checkout & Orders")
@allure.story("Place Order")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("TC16: Log in first, then place an order")
def test_place_order_login_before_checkout(
    base_url, home_page, login_page, cart_page, checkout_page, payment_page,
    order_placed_page, account_deleted_page, existing_user,
):
    user = existing_user

    home_page.load(base_url)
    home_page.expect_home_page_visible()

    home_page.navbar.go_to_login()
    login_page.login(user.email, user.password)

    home_page.navbar.expect_logged_in_as(user.name)

    home_page.add_product_to_cart_by_index(0)
    home_page.click_continue_shopping()

    home_page.navbar.go_to_cart()
    cart_page.expect_visible(cart_page.cart_rows.first, "cart page with added product")

    cart_page.click_proceed_to_checkout()

    checkout_page.expect_address_and_order_review_visible()
    checkout_page.enter_comment("Ring the bell on arrival.")
    checkout_page.place_order()

    payment_page.pay_with_test_card(user.name)

    order_placed_page.expect_order_placed_success()

    home_page.navbar.delete_account()
    account_deleted_page.expect_account_deleted()
