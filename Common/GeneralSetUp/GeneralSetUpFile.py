from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))



class SetUpClass():
    def generalSetUp(self):
        self.driver = driver
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)