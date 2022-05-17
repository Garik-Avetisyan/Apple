from Locators.LocatorsFile import *
from Common.CustomFind.FindElement import FindElement
import time

class CartPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)


    def delete_all_items_from_cart(self):
        cartItemsCount = self.findElement.find(*cartSectionDeleteButtonLocator)
        numberCartItemsCount = int(cartItemsCount.text)
        try:
            while numberCartItemsCount > 0:
                deleteItemsButton = self.driver.find_element(*cartSectionDeleteButtonLocator)
                deleteItemsButton.click()
                numberCartItemsCount -= 1
                time.sleep(2)
        except:
            pass