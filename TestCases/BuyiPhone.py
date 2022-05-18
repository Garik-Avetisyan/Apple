import time
import unittest
from Pages.MainPage import HomePageApple
from Common.GeneralSetUp.GeneralSetUpFile import SetUpClass
from Pages.SelectProductDetailsPage import SelectProductDetailsPage
from Pages.MainPage import CartPage


class BuyiPhone11Class(unittest.TestCase, SetUpClass):
    def setUp(self):
        self.generalSetUp()
        self.navigationbar = HomePageApple.NavigationBarClass(self.driver)
        self.chapterBar = HomePageApple.ChapterNavigationBarClass(self.driver)
        self.selectIphone = SelectProductDetailsPage.SelectProductDetailsPage(self.driver)
        self.cartPage = CartPage.CartPageClass(self.driver)

    def test_buy_iphone(self):
        self.driver.get("https://www.apple.com")
        self.assertEqual(self.driver.title, "Apple", "Error text")
        self.navigationbar.click_iphone_button()
        self.chapterBar.click_iphone_11_button()
        # self.selectIphone.choose_color()
        # self.selectIphone.choose_gb()
        # self.selectIphone.connect_on_your_own_later()
        # self.selectIphone.press_no()
        # self.selectIphone.one_time_payment()
        # self.selectIphone.scroll()
        # self.selectIphone.add_to_bag()

        self.navigationbar.click_bag_button()
        self.navigationbar.click_hidn_bag_button()

        self.cartPage.delete_all_items_from_cart()

    def tearDown(self):
        time.sleep(3)
        self.driver.close()
