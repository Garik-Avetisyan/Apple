from Common.CustomFind.FindElement import FindElement
from Locators.Locators import *
import time

class ProductDetailsPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def click_on_color_image(self):
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 500)")
        colorImage = self.findElement.find(*productDetailsPageColorImageLocator)
        colorImage.click()

    def click_on_add_to_bug_button(self):
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 500)")
        addToBugButton = self.findElement.find(*productDetailsPageAddToBagButtonLocator)
        addToBugButton.click()







