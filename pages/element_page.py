import time

from locators.elements_page_locator import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):

        self.element_is_visible(self.locators.FULL_NAME).send_keys('sdfsdf')
        self.element_is_visible(self.locators.EMAIL).send_keys('sfsfa@gmail.com')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('sfsfa')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('safasfa')
        self.go_to_element_2(self.locators.SUBMIT)
        self.element_is_clickable(self.locators.SUBMIT).click()