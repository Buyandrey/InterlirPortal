import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.chrome_options.add_argument("--no-sandbox")
        cls.chrome_options.add_argument("--start-maximized")
        cls.chrome_options.add_argument("--disable-dev-shm-usage")
        # cls.chrome_options.add_argument("--headless")

        cls.driver = webdriver.Chrome(options=cls.chrome_options)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("OK!")
