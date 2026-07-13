import allure


@allure.feature("Product Catalog")
@allure.story("Brands")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("TC19: Browse products via the brand sidebar")
def test_view_and_cart_brand_products(base_url, home_page, products_page, category_brand_page):
    home_page.load(base_url)
    home_page.expect_home_page_visible()

    home_page.navbar.go_to_products()

    products_page.sidebar.expect_brands_visible()

    products_page.sidebar.click_brand("Polo")
    category_brand_page.expect_heading_contains("Polo")
    category_brand_page.expect_products_visible()

    category_brand_page.sidebar.click_brand("H&M")
    category_brand_page.expect_heading_contains("H&M")
    category_brand_page.expect_products_visible()
