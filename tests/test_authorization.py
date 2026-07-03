from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.mark.registration
@pytest.mark.authorization
def test_wrong_email_or_password_authorization(chromium_page: Page):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    email_input_registration = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    email_input_registration.fill('user.name@gmail.com')

    password_input_registration = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    password_input_registration.fill('password')

    login_button = chromium_page.get_by_test_id('login-page-login-button')
    login_button.click()

    wrong_email_or_password = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password).to_be_visible()

