from Selenium import webdriver

class Set_Up_Class():
    def generalSetUp(self):
        self.driver = webdriver.Chrome("..\\Common\\Drivers\\chromedriver.exe")
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)