from selenium import webdriver
import time                       # for importing time related functions and real time
import unittest
import sys                        # when we have to run test cases on cmd(command line)
import os                         # when we have to run test cases on cmd(command line)
sys.path.append(os.path.join(os.path.dirname(__file__),"...","..."))         # when we have to run test cases on cmd(command line)
from page import Page                    # importing page class from page.py
from homepage import homepage            # importing homepage class from homepage.p

class LoginTest(unittest.TestCase):         #testcase will inherit the unittest to use its functions

    @classmethod
    def setUpClass(cls):                       # for opening web browser
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # for log in into the website "ORANGEHRM"
        login=Page(driver)
        login.enter_Username("Admin")
        login.enter_password("admin123")
        login.click_login()
        # for log out
        home=homepage(driver)
        home.click_polatAlemdar()
        home.click_logout()

        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()                       # close the website
        cls.driver.quit()                        # quit the web driver
        print("Test Completed")                  # to print "test completed" if test succesfully completed

