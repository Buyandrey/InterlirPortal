import HtmlTestRunner
import unittest

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from _Locators.locators import LoginPageLocators as lpl

EXPLICIT_WAIT_TIME = 3


class BasePage(unittest.TestCase):
    web_element = WebElement
    web_driver_wait = WebDriverWait
    web_driver = webdriver

    def __init__(self, driver):
        self.web_driver = driver

    def open(self, url):
        self.web_driver.get(url)
        return self



    def waitElementVisible(self, element):
        """
        Returns WebElement when it will be appeared.
        """
        self.web_driver_wait(self.driver, EXPLICIT_WAIT_TIME) \
            .until(expected_conditions.visibility_of(element))
        return element

    def find_by_xpath(self, xpath):
        """
        Returns WebElement when it will be found.
        """
        return self.driver.find_element(By.XPATH, xpath)

    def click_on(self, element_xpath):
        element = self.find_by_xpath(element_xpath)
        self.waitElementVisible(element) \
            .click()

    def set_value(self, element_xpath, value):
        element = self.find_by_xpath(element_xpath)
        self.waitElementVisible(element).clear()
        self.waitElementVisible(element).send_keys(value)
