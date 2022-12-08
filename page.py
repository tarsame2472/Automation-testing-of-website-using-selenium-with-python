from locator import Locators

class Page():

    def __init__(self, driver):
        self.driver = driver
        self.Username_textbox_xpath=Locators.Username_textbox_xpath
        self.password_textbox_xpath=Locators.password_textbox_xpath
        self.login_button_xpath =Locators.login_button_xpath

    def enter_Username(self, Username):
        self.driver.find_element("xpath",self.Username_textbox_xpath).clear()
        self.driver.find_element("xpath",self.Username_textbox_xpath).send_keys(Username)

    def enter_password(self, password):
        self.driver.find_element("xpath",self.password_textbox_xpath).clear()
        self.driver.find_element("xpath",self.password_textbox_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element("xpath", self.login_button_xpath).click()