import allure


@allure.feature("Cart")
@allure.story("Recommended Items")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("TC22: Add a recommended item to the cart from the home page")
def test_add_to_cart_from_recommended_items(base_url, home_page, cart_page):
    home_page.load(base_url)
    home_page.expect_home_page_visible()

    product_id = home_page.recommended_item_id(0)
    home_page.add_recommended_item_to_cart(0)
    home_page.click_view_cart_from_modal()

    cart_page.expect_product_in_cart(product_id)
