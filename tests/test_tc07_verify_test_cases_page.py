import allure


@allure.feature("Site Navigation")
@allure.story("Test Cases Page")
@allure.severity(allure.severity_level.MINOR)
@allure.title("TC7: The Test Cases page is reachable from the header")
def test_verify_test_cases_page(base_url, home_page, test_cases_page):
    home_page.load(base_url)
    home_page.expect_home_page_visible()

    home_page.navbar.go_to_test_cases()

    test_cases_page.expect_test_cases_page_visible()
