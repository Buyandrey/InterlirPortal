from _Locators.locators import LoginPageLocators as lpl
from _Pages._base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        # For possibility of search and interact with web page
        super().__init__(driver)
        self.driver = driver
        ''' List of web elements which can be used during autotests of login page:
        ========================================================================='''
        self.email_textfield_xpath      = lpl.email_textfield_xpath
        self.password_textfield_xpath   = lpl.password_textfield_xpath
        self.authorization_button_xpath = lpl.authorization_button_xpath
        self.registerHere_button_xpath  = lpl.registerHere_button_xpath
        '''======================================================================'''

    ''' Methods which can be used during autotests of login page:
    ======================================================================================'''

    def login_as(self, email, password):
        self.setEmail(email).setPassword(password).click_on(self.authorization_button_xpath)
        return self
    def setEmail(self, value):
        self.set_value(self.email_textfield_xpath, value)
        return self

    def setPassword(self, value):
        self.set_value(self.password_textfield_xpath, value)
        return self

    def clickAuthorizationButton(self):
        self.click_on(self.authorization_button_xpath)
        return self

    def clickARegistrationHereButton(self):
        self.click_on(self.registerHere_button_xpath)
        return self
    '''===================================================================================
    '''