from Common.CustomFind.FindElement import FindElement
from Locators.Locators import *
from selenium.webdriver.common.keys import Keys


class AccessoriesPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)


    def fill_search_field(self, text):
        self.driver.execute_script("window.scrollTo(0, 500)")
        searchField = self.findElement.find(*accessoriesPageSearchFieldLocator)
        searchField.click()
        searchField.send_keys(text)
        searchField.send_keys(Keys.ENTER)





