from Locators.Locators import *
from Common.CustomFind.FindElement import FindElement
import time

class CartPageGarikClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)


    def delete_one_item(self):
        dell = self.findElement.find(*dellButton)
        dell.click()


    def delete_all_items(self):
        num = self.findElement.find(*cartCount)
        time.sleep(1)
        try:
            x = int(num.text)
            while x > 0:
                dell = self.findElement.find(*dellButton)
                dell.click()
                x -= 1
                time.sleep(1)
            print("cart is empty")
        except:
            pass