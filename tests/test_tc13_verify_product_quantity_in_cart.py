import allure


@allure.feature("Cart")
@allure.story("Product Quantity")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("TC13: Increase quantity on the product page and verify it in the cart")
def test_verify_product_quantity_in_cart(base_url, home_page, product_detail_page, cart_page):
    home_page.load(base_url)
    home_page.expect_home_page_visible()

    product_id = home_page.product_cards.first.locator(".add-to-cart").first.get_attribute(
        "data-product-id"
    )
    home_page.view_product_by_index(0)

    product_detail_page.expect_product_details_visible()

    product_detail_page.set_quantity(4)
    product_detail_page.add_to_cart()
    product_detail_page.click_view_cart_from_modal()

    cart_page.expect_product_in_cart(int(product_id))
    with allure.step("Verify cart quantity is exactly 4"):
        assert cart_page.get_quantity(int(product_id)) == "4"
