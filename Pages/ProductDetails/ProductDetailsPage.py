from Locators.LocatorsFile import *
from Common.CustomFind.FindElement import FindElement

class buy_some_product():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def press_in_buy_button(self):
        buyButton = self.findElement.find(*buyBtn)
        buyButton.click()