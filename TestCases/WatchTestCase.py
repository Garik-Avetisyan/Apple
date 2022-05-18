import time
import unittest
from Common.GeneralSetUp.GeneralSetUpFile import SetUpClass
from Pages.MainPage.HomePageApple import NavigationBarClass
from Pages.MainPage.HomePageApple import ChapterNavigationBarClass
from Pages.ProductDetails.ProductDetailsPage import buy_some_product
from Pages.WatchesListAndDetailsPage.WatchesListPage import WatchesListPageClass
from Pages.WatchesListAndDetailsPage.WatchDetailsPage import WatchDetailsPageClass
from Pages.MainPage.CartPage import CartPageClass


class WatchTestClass(unittest.TestCase, SetUpClass):
    def SetUp(self):
        self.generalSetUp()
        self.navigationBar = NavigationBarClass(self.driver)
        self.chapterBar = ChapterNavigationBarClass(self.driver)
        self.buyProduct = buy_some_product(self.driver)
        self.watchesListPage = WatchesListPageClass(self.driver)
        self.watchDetailsPage = WatchDetailsPageClass(self.driver)
        self.cartPage = CartPageClass(self.driver)

    def test_buyWatchTC(self):
        self.driver.get("https://www.apple.com")
        self.navigationBar.click_watch_button()
        self.chapterBar.click_apple_watch_nike_button()

        self.buyProduct.press_in_buy_button()

        self.watchesListPage.click_into_watch()

        self.watchDetailsPage.press_color_button()
        self.watchDetailsPage.press_case_size_button()
        self.watchDetailsPage.press_connectivity_button()
        self.watchDetailsPage.scroll_down_2000()
        self.watchDetailsPage.press_add_to_bag_button()

        self.navigationBar.click_bag_button()
        self.navigationBar.click_hidn_bag_button()

        self.cartPage.delete_all_items_from_cart()

    def tearDown(self):
        time.sleep(1)
        self.driver.close()
