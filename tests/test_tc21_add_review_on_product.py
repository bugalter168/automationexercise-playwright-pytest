import allure

from utils.data_generator import fake, unique_email


@allure.feature("Product Catalog")
@allure.story("Product Reviews")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("TC21: Submit a review on a product")
def test_add_review_on_product(base_url, home_page, products_page, product_detail_page):
    home_page.load(base_url)

    home_page.navbar.go_to_products()
    products_page.expect_all_products_visible()

    products_page.view_product_by_index(0)

    product_detail_page.expect_visible(
        product_detail_page.write_review_heading, "'Write Your Review' tab"
    )

    product_detail_page.submit_review(
        name=fake.name(),
        email=unique_email("review"),
        review="This product exceeded my expectations during testing.",
    )

    product_detail_page.expect_review_success()
