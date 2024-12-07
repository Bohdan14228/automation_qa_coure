import random
import time

from locators.elements_page_locator import *
from pages.base_page import BasePage
from generator.generator import generated_person
from selenium.webdriver.support.ui import Select


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.go_to_element_2()
        self.element_is_clickable(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21

        # while count != 0:
        #     item = item_list[random.randint(1, 15)]
        #     if count > 0:
        #         self.go_to_element(item)
        #         item.click()
        #         count -= 1
        #         print(item.text)
        #     else:
        #         break

        while count != 0:
            item = item_list[random.randint(1, 15)]
            self.go_to_element(item)
            item.click()
            count -= 1

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(*self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(" ", '').replace("doc", '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonLocator()

    def click_on_the_radio_button(self, choice):
        choices = {
            'yes': self.locators.BUTTON_YES,
            'impressive': self.locators.BUTTON_IMPRESSIVE,
            'no': self.locators.BUTTON_NO
        }
        select_item = self.element_is_clickable(choices[choice])
        select_item.click()
        return select_item.text

    def read_selected(self):
        selected_item = self.element_is_visible(self.locators.SELECTED_BUTTON)
        return selected_item.text


class WebTablePage(BasePage):
    locators = WebTableLocator()

    def add_new_person(self, ):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()
            count -= 1
            return [firstname, lastname, str(age), email, str(salary), department]

    def check_new_added_person(self):
        person_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in person_list:
            data.append(item.text.splitlines())
        return data

    def search_some_person(self, key_word):
        self.go_to_element_2()
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.elements_are_present(self.locators.DELETE_BUTTON)[-1]
        row = delete_button.find_element(*self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.go_to_element_2('1000')
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []

        dropdown = Select(self.element_is_visible(self.locators.COUNT_ROW_LIST))
        for i in count:
            count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            dropdown.select_by_value(f"{i}")
            time.sleep(1)
            data.append(self.check_count_rows())
        return data

        # for x in count:
        #     count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST)
        #     self.go_to_element(count_row_button)
        #     count_row_button.click()
        #     self.element_is_visible(('css selector', f'option[value="{x}"]')).click()
        #     data.append()

    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)


class ButtonPage(BasePage):
    locators = ButtonsPageLocators()

    def click_on_different_button(self, type_click):
        # button = self.element_is_visible(self.locators.CLICK_ME_BUTTON)
        # self.go_to_element(button)
        # self.go_to_element_2("2000")
        # self.action_scroll(button)
        if type_click == 'double':
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_DOUBLE)
        if type_click == 'right':
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_RIGHT)
        if type_click == 'click':
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(self.locators.SUCCESS_CLICK_ME)

    def check_clicked_on_the_button(self, element):
        return self.element_is_present(element).text

    def scroll_to_button(self):
        button = self.element_is_visible(self.locators.CLICK_ME_BUTTON)
        self.action_scroll(button)