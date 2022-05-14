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
        self.navigationbar.click_watch_button()

    def tearDown(self):
        time.sleep(3)
        self.driver.close()
