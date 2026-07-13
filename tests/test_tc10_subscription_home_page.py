import allure

from utils.data_generator import unique_email


@allure.feature("Subscription")
@allure.story("Home Page")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("TC10: Subscribe to the newsletter from the home page footer")
def test_subscription_home_page(base_url, home_page):
    home_page.load(base_url)
    home_page.expect_home_page_visible()

    home_page.subscription.subscribe(unique_email("subscribe"))

    home_page.subscription.expect_subscribed_successfully()
