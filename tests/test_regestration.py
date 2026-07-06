import pytest
from playwright.sync_api import sync_playwright, expect, Page

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page, registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.fill_registration_form(email='user@gm.com', password='asds', username='vlad')
    registration_page.click_registration_button()
    dashboard_page.check_visible_dashboard_title()