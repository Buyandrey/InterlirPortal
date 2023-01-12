import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".", "."))
import unittest
import time
import HtmlTestRunner
from selenium.webdriver.chrome.options import Options
from _Tests._base_test import BaseTest
from _Pages.login_page import LoginPage
from resources.constants import URL


class LoginTest(BaseTest, unittest.TestCase):
    chrome_options = Options()
    driver = None
    url = "https://portal-dev.interlir.ninja/login"

    def test_correct_login(self):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.open(URL.LOGIN_URL)
        login_page.login_as("buyandrey96w@gmail.com", "testPassword123")

        time.sleep(2)


''' 
Next lines are for running unittest from commandline without keys "-m unittest" 
and for generate html reports.
'''
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/bans/Projects/Python/_InterlirPortal/reports"))
