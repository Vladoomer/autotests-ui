from playwright.sync_api import Page,Route


def mock_static_resource(page: Page):
    page.route("**/*.{ico,png,jpeg,jpg,svg,webp,mp3,mp4,woff,woff2}", lambda route: route.abort())