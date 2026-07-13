import allure


@allure.feature("Cart")
@allure.story("Add Products")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("TC12: Add two products to the cart and verify price, quantity and total")
def test_add_products_in_cart(base_url, home_page, products_page, cart_page):
    home_page.load(base_url)
    home_page.expect_home_page_visible()

    home_page.navbar.go_to_products()

    first_product_id = products_page.product_id_by_index(0)
    products_page.add_product_to_cart_by_index(0)
    products_page.click_continue_shopping()

    second_product_id = products_page.product_id_by_index(1)
    products_page.add_product_to_cart_by_index(1)
    products_page.click_view_cart_from_modal()

    cart_page.expect_product_in_cart(first_product_id)
    cart_page.expect_product_in_cart(second_product_id)

    for product_id in (first_product_id, second_product_id):
        with allure.step(f"Verify price, quantity and total for product {product_id}"):
            assert cart_page.get_quantity(product_id) == "1"
            price = cart_page.get_price(product_id)
            total = cart_page.get_total(product_id)
            assert price == total
