import allure

from utils.data_generator import unique_email


@allure.feature("Subscription")
@allure.story("Cart Page")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("TC11: Subscribe to the newsletter from the cart page footer")
def test_subscription_cart_page(base_url, home_page, cart_page):
    home_page.load(base_url)
    home_page.expect_home_page_visible()

    home_page.navbar.go_to_cart()

    cart_page.subscription.subscribe(unique_email("subscribe"))

    cart_page.subscription.expect_subscribed_successfully()
