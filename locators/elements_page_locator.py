from selenium.webdriver.common.by import By

class TextBoxPageLocators:
    FULL_NAME = ('css selector', "input[id='userName']")
    EMAIL = ('css selector', "input[id='userEmail']")
    CURRENT_ADDRESS = ('css selector', "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = ('css selector', "textarea[id='permanentAddress']")
    SUBMIT = ('css selector', "button[id='submit']")

    CREATED_FULL_NAME = ('css selector', "#output #name")
    CREATED_EMAIL = ('css selector', "#output #email")
    CREATED_CURRENT_ADDRESS = ('css selector', "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = ('css selector', "#output #permanentAddress")


class CheckBoxLocators:
    EXPAND_ALL_BUTTON = ('css selector', "button[title='Expand all']")
    ITEM_LIST = ("css selector", "span[class='rct-title']")
    CHECKED_ITEMS = ('css selector', "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ('xpath', ".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = ('css selector', "span[class='text-success']")

    #2:12:30