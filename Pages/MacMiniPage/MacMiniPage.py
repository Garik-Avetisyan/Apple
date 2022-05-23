from Locators.Locators import *
from Common.CustomFind.FindElement import FindElement

class MacMiniClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def press_on_select_button(self):
        self.driver.execute_script("window.scrollTo(0, 2000)")
        selectButton = self.findElement.find(*selectMacMiniLocator)
        selectButton.click()

    def press_on_continue(self):
        continueButton = self.findElement.find(*continueButtonLocator)
        continueButton.click()

    def press_on_add_to_bag_button(self):
        addToBag = self.findElement.find(*addToBagButtonLocator)
        addToBag.click()
