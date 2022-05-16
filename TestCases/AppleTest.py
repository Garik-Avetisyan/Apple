import time
import unittest
from Pages.MainPage.HomePageApple import NavigationBarClass
from Common.GeneralSetUp.GeneralSetUpFile import SetUpClass

class AppleTestClass(unittest.TestCase, SetUpClass):
    def setUp(self):
        self.generalSetUp()
        self.navigationbar = NavigationBarClass(self.driver)

    def test_simpleTC(self):
        self.driver.get("https://www.apple.com")
        self.navigationbar.click_mac_button()
        self.navigationbar.click_iphone_button()
        self.navigationbar.click_ipad_button()
        self.navigationbar.click_watch_button()
        self.navigationbar.click_airpods_button()
        self.navigationbar.click_tv_home_button()
        self.navigationbar.click_only_on_apple_button()
        self.navigationbar.click_accessories_button()
        self.navigationbar.click_bag_button()
        self.navigationbar.click_hidn_bag_button()



    def tearDown(self):
        time.sleep(3)
        self.driver.close()
