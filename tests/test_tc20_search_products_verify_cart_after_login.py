import allure


@allure.feature("Cart")
@allure.story("Cart Persistence")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("TC20: Search products, add to cart, and verify the cart survives login")
def test_search_products_verify_cart_after_login(
    base_url, home_page, products_page, cart_page, login_page, existing_user,
):
    user = existing_user

    home_page.load(base_url)
    home_page.navbar.go_to_products()
    products_page.expect_all_products_visible()

    products_page.search_product("Dress")
    products_page.expect_searched_products_visible()
    products_page.expect_products_visible()

    product_id = products_page.product_id_by_index(0)
    products_page.add_product_to_cart_by_index(0)
    products_page.click_view_cart_from_modal()

    cart_page.expect_product_in_cart(product_id)

    home_page.navbar.go_to_login()
    login_page.login(user.email, user.password)
    home_page.navbar.expect_logged_in_as(user.name)

    home_page.navbar.go_to_cart()
    cart_page.expect_product_in_cart(product_id)
