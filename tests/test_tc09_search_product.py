import allure


@allure.feature("Product Catalog")
@allure.story("Search Product")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("TC9: Search for a product and verify matching results")
def test_search_product(base_url, home_page, products_page):
    home_page.load(base_url)
    home_page.expect_home_page_visible()

    home_page.navbar.go_to_products()
    products_page.expect_all_products_visible()

    products_page.search_product("Top")

    products_page.expect_searched_products_visible()
    products_page.expect_products_visible()
