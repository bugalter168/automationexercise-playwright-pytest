import allure


@allure.feature("Product Catalog")
@allure.story("All Products")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("TC8: Browse All Products and open the first product's detail page")
def test_all_products_and_detail_page(base_url, home_page, products_page, product_detail_page):
    home_page.load(base_url)
    home_page.expect_home_page_visible()

    home_page.navbar.go_to_products()
    products_page.expect_all_products_visible()

    products_page.view_product_by_index(0)

    product_detail_page.expect_product_details_visible()
