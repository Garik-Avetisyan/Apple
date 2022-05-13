import time
from Common.CustomFind.FindElement import FindElement
from LocatorsFile.Locators import *

class SelectProductDetailsPage():
    def __init__(self, driver):
        self.driver = driver
        self.FindElement = FindElement(self.driver)

    def choose_color(self):
        chooseColor = self.FindElement.find(*blackColor)
        chooseColor.click()
        time.sleep(1)

    def choose_gb(self):
        chooseGB = self.FindElement.find(*gb64)
        chooseGB.click()
        time.sleep(1)

    def connect_on_your_own_later(self):
        clickOnIt = self.FindElement.find(*connectLoc)
        clickOnIt.click()
        time.sleep(1)

    def press_no(self):
        pressNo = self.driver.find_element(*pressNO)
        pressNo.click()
        time.sleep(1)

    def one_time_payment(self):
        oneTimePay = self.FindElement.find(*oneTimePayment)
        oneTimePay.click()

    def scroll(self):
        scroll = self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight, 500)")
        return scroll

    def add_to_bag(self):
        time.sleep(2)
        addToBag = self.FindElement.find(*addBag)
        addToBag.click()

