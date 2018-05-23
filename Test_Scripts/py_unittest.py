#Unittest framework Script with Python and Selenium
#Date : 7th May 2018

import unittest
import time
from selenium import webdriver
# Importing Options to invoke the Headless Browser session
from selenium.webdriver.firefox.options import Options


class py_unittest(unittest.TestCase):
    def setUp(self):
        global driver
        global browser
        # Code for headless Browser invoking
        # opts = Options()
        # opts.set_headless()
        # assert opts.headless
        # driver = webdriver.Firefox(options=opts,
                                   # executable_path=r'C:\\Users\HP User\PycharmProjects\FirstTest\drivers\geckodriver.exe')
        # print("Firefox Headless Browser Invoked")
        Code for calling Firefox Browser
        driver = webdriver.Firefox(
        executable_path = r'C:\\Users\HP User\PycharmProjects\FirstTest\drivers\geckodriver.exe')

    def test_search(self):
        driver.get("https://www.python.org/")
        assert "Python" in driver.title
        driver.implicitly_wait(30)
        driver.maximize_window()
        self.element = driver.find_element_by_name("q")
        self.element.clear()
        self.element.send_keys("PyCon")
        self.element.click()
        time.sleep(10)

    def test_google(self):
        driver.get("http://google.com")
        if not "Google" in driver.title:
            raise Exception("Unable to load Google Page")
        self.element = driver.find_element_by_name("q")
        self.element.send_keys("TestingBot")
        self.element.submit()
        time.sleep(10)

    def tearDown(self):
        driver.close()


if __name__ == '__main__':
    unittest.main()
