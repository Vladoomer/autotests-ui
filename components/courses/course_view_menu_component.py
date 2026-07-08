from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.button import Button


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button(page, 'course-view-menu-button', "Menu button")
        self.edit_menu_item = Button(page, 'course-view-edit-menu-item', "Edit button")
        self.delete_menu_item = Button(page, 'course-view-delete-menu-item', "Delete button")

    def click_edit(self, index: int):
        expect(self.menu_button).to_be_visible()
        self.menu_button.nth(index).click()
        expect(self.edit_menu_item).to_be_visible()
        self.edit_menu_item.nth(index).click()

    def click_delete(self, index: int):
        expect(self.menu_button).to_be_visible()
        self.menu_button.nth(index).click()
        expect(self.delete_menu_item).to_be_visible()
        self.delete_menu_item.nth(index).click()