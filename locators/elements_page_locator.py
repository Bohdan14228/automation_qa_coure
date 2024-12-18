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


class RadioButtonLocator:
    BUTTON_YES = ('css selector', "label[for='yesRadio']")
    BUTTON_IMPRESSIVE = ('css selector', "label[for ='impressiveRadio']")
    BUTTON_NO = ('css selector', "label[for ='noRadio']")
    SELECTED_BUTTON = ('css selector', "span[class='text-success']")


class WebTableLocator:
    #add person form
    ADD_BUTTON = ('css selector', "button[id='addNewRecordButton']")
    FIRSTNAME_INPUT = ('css selector', "input[id='firstName']")
    LASTNAME_INPUT = ('css selector', "input[id='lastName']")
    EMAIL_INPUT = ('css selector', "input[id='userEmail']")
    AGE_INPUT = ('css selector', "input[id='age']")
    SALARY_INPUT = ('css selector', "input[id='salary']")
    DEPARTMENT_INPUT = ('css selector', "input[id='department']")
    SUBMIT = ('css selector', "button[id='submit']")

    #tables
    FULL_PEOPLE_LIST = ('css selector', "div[class='rt-tr-group']")
    SEARCH_INPUT = ('css selector', "input[id='searchBox']")
    DELETE_BUTTON = ('css selector', "span[title='Delete']")
    ROW_PARENT = ('xpath', ".//ancestor::div[@class='rt-tr-group']")
    NO_ROWS_FOUND = ('css selector', "div[class='rt-noData']")
    COUNT_ROW_LIST = ('css selector', 'select[aria-label="rows per page"]')

    #update
    UPDATE_BUTTON = ('css selector', "span[title='Edit']")


class ButtonsPageLocators:
    DOUBLE_BUTTON = ('css selector', 'button[id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = ('css selector', 'button[id="rightClickBtn"]')
    CLICK_ME_BUTTON = ('xpath', '//div[3]/button')

    #result
    SUCCESS_DOUBLE = ('css selector', 'p[id="doubleClickMessage"]')
    SUCCESS_RIGHT = ('css selector', 'p[id="rightClickMessage"]')
    SUCCESS_CLICK_ME = ('css selector', 'p[id="dynamicClickMessage"]')


class LinksPageLocators:
    SIMPLE_LINK = ('css selector', "a[id='simpleLink']")
    BAD_REQUEST = ('css selector', "a[id='bad-request']")


class UploadAndDownloadLocators:
    UPLOAD_FILE = ('css selector', "input[id='uploadFile']")
    UPLOADED_FILE = ("css selector", "p[id='uploadedFilePath']")
    DOWNLOAD_FILE = ('css selector', "a[id='downloadButton']")


class DynamicPropertiesPageLocators:
    COLOR_CHANGE_BUTTON = ('css selector', 'button[id="colorChange"]')
    COLOR_AFTER_FIVE_SEC_BUTTON = ('css selector', 'button[id="visibleAfter"]')
    ENABLE_BUTTON = ('css selector', 'button[id="enableAfter"]')





