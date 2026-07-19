import allure
import pytest
from allure_commons.types import Severity
from playwright.sync_api import Page

from config import settings
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.registration
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.DASHBOARD)
@allure.sub_suite(AllureStory.DASHBOARD)
@allure.tag(AllureTag.REGISTRATION, AllureTag.REGRESSION)
class TestRegistration:
    @allure.title("Registration with correct email, username and password")
    @allure.severity(Severity.BLOCKER)
    def test_successful_registration(self, chromium_page: Page, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.fill(email=settings.test_user.email,
                                                 password=settings.test_user.password,
                                                 username=settings.test_user.username)
        registration_page.registration_form.check_visible(email=settings.test_user.email,
                                                 password=settings.test_user.password,
                                                 username=settings.test_user.username)
        registration_page.click_registration_button()
        dashboard_page.toolbar_view.check_visible()