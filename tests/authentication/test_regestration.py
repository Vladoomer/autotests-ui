import pytest
from playwright.sync_api import Page

from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage


@pytest.mark.regression
@pytest.mark.registration
class TestRegistration:
    def test_successful_registration(self, chromium_page: Page, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email='user@gm.com', password='asds', username='vlad')
        registration_page.registration_form.check_visible(email='user@gm.com', password='asds', username='vlad')
        registration_page.click_registration_button()
        dashboard_page.toolbar_view.check_visible()