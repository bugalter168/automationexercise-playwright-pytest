import allure


@allure.feature("Cart")
@allure.story("Remove Products")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("TC17: Remove a product from the cart")
def test_remove_products_from_cart(base_url, home_page, products_page, cart_page):
    home_page.load(base_url)
    home_page.expect_home_page_visible()

    home_page.navbar.go_to_products()
    product_id = products_page.product_id_by_index(0)
    products_page.add_product_to_cart_by_index(0)
    products_page.click_view_cart_from_modal()

    cart_page.expect_product_in_cart(product_id)

    cart_page.remove_product(product_id)

    cart_page.expect_product_not_in_cart(product_id)
