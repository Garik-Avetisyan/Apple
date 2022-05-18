import time
from Common.CustomFind.FindElement import FindElement
from Locators.Locators import *


class WatchDetailsPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def press_color_button(self):
        watchColor = self.findElement.find(*watchColorLocator)
        watchColor.click()
        time.sleep(1)

    def press_case_size_button(self):
        caseSize = self.findElement.find(*caseSizeLocator)
        caseSize.click()
        time.sleep(1)

    def press_connectivity_button(self):
        gpsOrGpsCellular = self.findElement.find(*gpsOrGpsCellularLocator)
        gpsOrGpsCellular.click()
        time.sleep(1)

    def scroll_down_2000(self):
        self.driver.execute_script("window.scrollTo(0, 2000)")

    def press_add_to_bag_button(self):
        time.sleep(2)
        bagButton = self.findElement.find(*bagButtonLocator)
        bagButton.click()
