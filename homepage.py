class homepage():

    def __init__(self,driver):
        self.driver=driver
        self.polatAlemdar_link_xpath="//html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span"
        self.logout_link_xpath="//html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a"

    def click_polatAlemdar(self):
        self.driver.find_element("xpath",self.polatAlemdar_link_xpath).click()

    def click_logout(self):
        self.driver.find_element("xpath",self.logout_link_xpath).click()