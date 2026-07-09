import allure

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page:Page):
        super().__init__(page)

        self.email = Input(page, 'registration-form-email-input', "Email")
        self.username = Input(page, "registration-form-username-input", "Username")
        self.password = Input(page, 'registration-form-password-input', "Password")

    @allure.step("Fill registration form")
    def fill(self, email:str, username: str, password: str):
        self.email.fill(email)
        self.username.fill(username)
        self.password.fill(password)

    @allure.step("Check visible registration form")
    def check_visible(self, email:str, username: str, password: str):
        self.email.check_visible()
        self.email.check_have_value(email)

        self.username.check_visible()
        self.username.check_have_value(username)

        self.password.check_visible()
        self.password.check_have_value(password)