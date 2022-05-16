from Common.CustomFind.FindElement import FindElement
from Locators.Locators import *


class WatchesListPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def scroll_down_700(self):
        try:
            self.driver.execute_script("window.scrollTo(0, 700)")
        except:
            pass

    def click_into_watch(self):
        firstWatch = self.findElement.find(*firstWatchLocator)
        firstWatch.click()
