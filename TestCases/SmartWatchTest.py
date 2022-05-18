import time
import unittest
from selenium import webdriver
from Pages.WatchesListAndDetailsPage.WatchDetailsPage import WatchDetailsPageClass
from Pages.WatchesListAndDetailsPage.WatchesListPage import WatchesListPageClass


class WatchesPageTC(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../Common/Driver/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(20)
        self.watchesListPage = WatchesListPageClass(self.driver)
        self.watchDetailsPage = WatchDetailsPageClass(self.driver)

    def test_WatchTC(self):
        self.driver.get("https://www.apple.com/shop/buy-watch/apple-watch-nike")
        self.watchesListPage.click_into_watch()
        self.watchDetailsPage.press_color_button()
        self.watchDetailsPage.press_case_size_button()
        self.watchDetailsPage.press_connectivity_button()
        self.watchDetailsPage.scroll_down_2000()
        self.watchDetailsPage.press_add_to_bag_button()

    def tearDown(self):
        time.sleep(1)
        self.driver.close()
