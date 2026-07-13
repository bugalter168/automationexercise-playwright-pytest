import allure

from utils.data_generator import fake, unique_email


@allure.feature("Contact Us")
@allure.story("Contact Form")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("TC6: Submit the Contact Us form with a file attachment")
def test_contact_us_form(base_url, home_page, contact_page, sample_upload_file):
    home_page.load(base_url)
    home_page.expect_home_page_visible()

    home_page.navbar.go_to_contact_us()
    contact_page.expect_get_in_touch_visible()

    contact_page.fill_form(
        name=fake.name(),
        email=unique_email("contact"),
        subject="Automated test enquiry",
        message="This message was submitted by an automated Playwright test.",
        file_path=sample_upload_file,
    )
    contact_page.submit()

    contact_page.expect_success_message()

    contact_page.click_home()
    home_page.expect_home_page_visible()
