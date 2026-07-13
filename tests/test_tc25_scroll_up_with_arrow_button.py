import allure


@allure.feature("Site Navigation")
@allure.story("Scrolling")
@allure.severity(allure.severity_level.MINOR)
@allure.title("TC25: Scroll to the bottom, then back up using the arrow button")
def test_scroll_up_using_arrow_button(base_url, home_page):
    home_page.load(base_url)
    home_page.expect_home_page_visible()

    home_page.scroll_to_bottom()
    home_page.subscription.expect_visible(home_page.subscription.heading, "Subscription heading")

    home_page.scroll_up_via_arrow()

    home_page.expect_home_page_visible()
