class TextBoxPageLocators:
    FULL_NAME = ('css selector', "input[id='userName']")
    EMAIL = ('css selector', "input[id='userEmail']")
    CURRENT_ADDRESS = ('css selector', "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = ('css selector', "textarea[id='permanentAddress']")
    SUBMIT = ('css selector', "button[id='submit']")

    CREATED_FULL_NAME = ('css selector', "#output #name")
    CREATED_EMAIL = ('css selector', "#output #email")
    CREATED_CURRENT_ADDRESS = ('css selector', "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = ('css selector', "input[id='permanentAddress']")
