from Common.CustomFind.FindElement import FindElement
from Locators.Locators import *


class SearchResultsPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def click_on_first_product(self):
        firstProduct = self.findElement.find(*searchResultsPageFirstProductLocator)
        firstProduct.click()







