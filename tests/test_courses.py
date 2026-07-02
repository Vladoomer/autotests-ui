from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()  # Создание контекста
        page = context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        registration_button = page.get_by_test_id("registration-page-registration-button")
        # expect(registration_button).to_be_disabled()

        email_input_registration = page.get_by_test_id("registration-form-email-input").locator('input')
        email_input_registration.fill("user.name@gmail.com")

        username_input_registration = page.get_by_test_id("registration-form-username-input").locator('input')
        username_input_registration.fill("username")
        password_input_registration = page.get_by_test_id("registration-form-password-input").locator('input')
        password_input_registration.fill("password")

        # expect(email_input_registration).not_to_be_disabled()
        registration_button.click()
        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text('Courses')

        no_results_text = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(no_results_text).to_be_visible()
        expect(no_results_text).to_have_text('There is no results')
