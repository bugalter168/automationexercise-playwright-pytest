import re

import allure
from playwright.sync_api import Locator, Page, expect


class BasePage:
    """Wraps Playwright actions with Allure steps and screenshot attachments."""

    def __init__(self, page: Page):
        self.page = page

    def _attach_screenshot(self, name: str) -> None:
        try:
            self.page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        try:
            allure.attach(
                self.page.screenshot(),
                name=name,
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception:
            pass

    def goto(self, url: str) -> None:
        with allure.step(f"Navigate to {url}"):
            self.page.goto(url)
            self._attach_screenshot(f"goto - {url}")

    def click(self, locator: Locator, description: str) -> None:
        with allure.step(f"Click on {description}"):
            locator.scroll_into_view_if_needed()
            locator.click()
            self._attach_screenshot(f"click - {description}")

    def force_click(self, locator: Locator, description: str) -> None:
        with allure.step(f"Click on {description} (forced)"):
            locator.scroll_into_view_if_needed()
            locator.click(force=True)
            self._attach_screenshot(f"click - {description}")

    def fill(self, locator: Locator, text: str, description: str) -> None:
        with allure.step(f"Fill '{description}' with '{text}'"):
            locator.scroll_into_view_if_needed()
            locator.fill(text)
            self._attach_screenshot(f"fill - {description}")

    def check(self, locator: Locator, description: str) -> None:
        with allure.step(f"Check '{description}'"):
            locator.scroll_into_view_if_needed()
            locator.check()
            self._attach_screenshot(f"check - {description}")

    def hover(self, locator: Locator, description: str) -> None:
        with allure.step(f"Hover over '{description}'"):
            locator.scroll_into_view_if_needed()
            locator.hover()
            self._attach_screenshot(f"hover - {description}")

    def select_option(self, locator: Locator, value: str, description: str) -> None:
        with allure.step(f"Select '{value}' in '{description}'"):
            locator.select_option(value)
            self._attach_screenshot(f"select - {description}")

    def upload_file(self, locator: Locator, file_path: str, description: str) -> None:
        with allure.step(f"Upload file for '{description}'"):
            locator.set_input_files(file_path)
            self._attach_screenshot(f"upload - {description}")

    def get_text(self, locator: Locator) -> str:
        return locator.inner_text()

    def scroll_to_bottom(self) -> None:
        with allure.step("Scroll to bottom of page"):
            self.page.keyboard.press("End")
            self.page.wait_for_timeout(300)
            self._attach_screenshot("scroll - bottom")

    def scroll_to_top(self) -> None:
        with allure.step("Scroll to top of page"):
            self.page.keyboard.press("Home")
            self.page.wait_for_timeout(300)
            self._attach_screenshot("scroll - top")

    def expect_visible(self, locator: Locator, description: str) -> None:
        with allure.step(f"Verify '{description}' is visible"):
            expect(locator).to_be_visible()
            self._attach_screenshot(f"verify visible - {description}")

    def expect_hidden(self, locator: Locator, description: str) -> None:
        with allure.step(f"Verify '{description}' is not visible"):
            expect(locator).to_be_hidden()
            self._attach_screenshot(f"verify hidden - {description}")

    def expect_text(self, locator: Locator, text: str, description: str) -> None:
        with allure.step(f"Verify '{description}' contains text '{text}'"):
            expect(locator).to_contain_text(text)
            self._attach_screenshot(f"verify text - {description}")

    def expect_count(self, locator: Locator, count: int, description: str) -> None:
        with allure.step(f"Verify '{description}' has {count} item(s)"):
            expect(locator).to_have_count(count)
            self._attach_screenshot(f"verify count - {description}")

    def expect_url_contains(self, fragment: str) -> None:
        with allure.step(f"Verify page URL contains '{fragment}'"):
            expect(self.page).to_have_url(re.compile(re.escape(fragment)))
            self._attach_screenshot(f"verify url - {fragment}")
