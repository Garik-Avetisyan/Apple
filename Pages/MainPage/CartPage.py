from Apple.LocatorsFile.AppleLocators import *
from Common.CustumFind.FindElement import FindElement
import time

class CartPageClass():
    def __init__(self, driver):
        self.driver = driver

    def delete_all_items_from_cart(self):
        cartItemsCount = self.driver.find_element(*mainPageCartSectionButtonLocator)
        numberCartItemsCount = int(cartItemsCount.text)
        try:
            while numberCartItemsCount > 0:
                deleteItemsButton = self.driver.find_element(*cartSectionDeleteButtonLocatorAll)
                deleteItemsButton.click()
                numberCartItemsCount -= 1
                time.sleep(2)
        except:
            pass