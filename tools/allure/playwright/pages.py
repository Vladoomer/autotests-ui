import allure
from playwright.sync_api import Page, Playwright
from config import settings, Browser
from tools.allure.playwright.mocks import mock_static_resource


def initialize_playwright_pages(
        playwright: Playwright,
        browser_type: Browser,
        storage_state: str | None = None
    ) -> Page:

    browser = playwright[browser_type].launch(headless=settings.headless)
    context = browser.new_context(
        base_url=settings.get_base_url(),
        storage_state=storage_state,
        record_video_dir=settings.videos_dir
    )
    page = context.new_page()
    mock_static_resource(page)

    yield page
    browser.close()

    allure.attach.file(page.video.path(), name="video", attachment_type=allure.attachment_type.WEBM)