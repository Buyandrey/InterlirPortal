import unittest
from selenium import webdriver
from resources.configuration import Configurations as cfg


class BaseTest(unittest.TestCase):

    driver = None
    chrome_options = None

    @classmethod
    def setUpClass(cls):
        cls.chrome_options.add_argument("--no-sandbox")
        cls.chrome_options.add_argument("--start-maximized")
        cls.chrome_options.add_argument("--disable-dev-shm-usage")
        if cfg.HEADLESS:
            cls.chrome_options.add_argument("--headless")
        cls.driver = webdriver.Chrome(options=cls.chrome_options)
        cls.driver.implicitly_wait(10)
    @classmethod
    def tearDownClass(cls):
        if not cfg.HOLD_BROWSER_OPEN:
            cls.driver.close()
            cls.driver.quit()
