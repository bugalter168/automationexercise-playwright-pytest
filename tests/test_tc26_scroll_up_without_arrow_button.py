import allure


@allure.feature("Site Navigation")
@allure.story("Scrolling")
@allure.severity(allure.severity_level.MINOR)
@allure.title("TC26: Scroll to the bottom, then back up without the arrow button")
def test_scroll_up_without_arrow_button(base_url, home_page):
    home_page.load(base_url)
    home_page.expect_home_page_visible()

    home_page.scroll_to_bottom()
    home_page.subscription.expect_visible(home_page.subscription.heading, "Subscription heading")

    home_page.scroll_to_top()

    # The hero text sits in a rotating carousel, so right after scrolling it
    # can briefly be mid-transition (hidden) under slower/parallel CI runs —
    # same class of timing issue stabilized for TC20; give it more headroom
    # instead of a hardcoded sleep.
    home_page.expect_home_page_visible(timeout=15000)
