import allure


@allure.feature("Product Catalog")
@allure.story("Categories")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("TC18: Browse products via the Women and Men category sidebar")
def test_view_category_products(base_url, home_page, category_brand_page):
    home_page.load(base_url)

    home_page.sidebar.expect_visible(home_page.sidebar.women_toggle, "categories sidebar")

    home_page.sidebar.open_women_category()
    home_page.sidebar.click_category_link("Dress")

    category_brand_page.expect_heading_contains("Women")
    category_brand_page.expect_heading_contains("Dress")
    category_brand_page.expect_products_visible()

    category_brand_page.sidebar.open_men_category()
    category_brand_page.sidebar.click_category_link("Tshirts")

    category_brand_page.expect_heading_contains("Men")
    category_brand_page.expect_heading_contains("Tshirts")
    category_brand_page.expect_products_visible()
