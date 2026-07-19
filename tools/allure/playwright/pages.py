import allure
from playwright.sync_api import Page, Playwright


def initialize_playwright_pages(
        playwright: Playwright,
        storage_state: str | None = None

) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=storage_state, record_video_dir='./videos')
    page = context.new_page()

    yield page
    browser.close()

    allure.attach.file(page.video.path(), name="video", attachment_type=allure.attachment_type.WEBM)