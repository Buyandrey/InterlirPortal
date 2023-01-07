from _Locators.locators import RegistrationPageLocators as rpl
from _Pages._base_page import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):

    def __init__(self, driver):
        # For possibility of search and interact with web page
        self.driver = driver

        ''' List of web elements which can be used during autotests of registration page:
        ========================================================================='''
        self.email_textfield_xpath = rpl.email_textfield_xpath
        self.password_textfield_xpath = rpl.password_textfield_xpath
        self.registerNow_button_xpath = rpl.registerNow_button_xpath
        self.check_message_xpath = rpl.check_message_xpath
        self.already_message_xpath = rpl.already_message_xpath
        '''======================================================================'''

    ''' Methods which can be used during autotests of login page:
    ======================================================================================'''

    def setEmail(self, value):
        self.set_value(self.email_textfield_xpath, value)
        return self

    def setPassword(self, value):
        self.set_value(self.password_textfield_xpath, value)
        return self

    def clickARegistrationNowButton(self):
        self.click_on(self.registerNow_button_xpath)
        return self

    def checkMessageCheckEmail(self):
        return self.driver.find_element(By.XPATH, self.check_message_xpath).is_displayed()

    def checkMessageAlreadyExists(self):
        return self.driver.find_element(By.XPATH, self.already_message_xpath()).is_displayed()

    '''===================================================================================
    '''
