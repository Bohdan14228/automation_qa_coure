import random


class FormPageLocators:
    FIRST_NAME = ('css selector', 'input[id="firstName"]')
    LAST_NAME = ('css selector', 'input[id="lastName"]')
    EMAIL = ('css selector', 'input[id="userEmail"]')
    GENDER = ('css selector', f'label[for="gender-radio-{random.randint(1, 3)}"]')
    MOBILE = ('css selector', 'input[id="userEmail"]')
    DATE_OF_BIRTH = ('css selector', 'input[id="dateOfBirthInput"]')

