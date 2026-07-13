import allure


@allure.feature("Checkout & Orders")
@allure.story("Invoice")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("TC24: Download the invoice after placing an order")
def test_download_invoice_after_purchase(
    base_url, home_page, products_page, cart_page, login_page, signup_page,
    account_created_page, checkout_page, payment_page, order_placed_page,
    account_deleted_page, registered_user,
):
    user = registered_user

    home_page.load(base_url)
    home_page.expect_home_page_visible()

    home_page.add_product_to_cart_by_index(0)
    home_page.click_continue_shopping()

    home_page.navbar.go_to_cart()
    cart_page.click_proceed_to_checkout()
    cart_page.expect_checkout_login_prompt_visible()
    cart_page.click_register_login_in_modal()

    login_page.signup(user.name, user.email)
    signup_page.expect_account_information_visible()
    signup_page.fill_account_information(user)
    signup_page.submit_create_account()

    account_created_page.expect_account_created()
    account_created_page.click_continue()

    home_page.navbar.expect_logged_in_as(user.name)

    home_page.navbar.go_to_cart()
    cart_page.click_proceed_to_checkout()

    checkout_page.expect_address_and_order_review_visible()
    checkout_page.enter_comment("Please include a gift receipt.")
    checkout_page.place_order()

    payment_page.pay_with_test_card(user.name)

    order_placed_page.expect_order_placed_success()

    download = order_placed_page.download_invoice()
    with allure.step("Verify invoice file downloaded successfully"):
        assert "invoice" in download.suggested_filename.lower()

    order_placed_page.click_continue()

    home_page.navbar.delete_account()
    account_deleted_page.expect_account_deleted()
    account_deleted_page.click_continue()
