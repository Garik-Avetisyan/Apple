import time
import unittest
from Apple.Pages.MainPage.HomePageApple import NavigationBarClass
from Apple.Common.GeneralSetUp.GenSetUp import SetUpClass

class AppleTestClass(unittest.TestCase, SetUpClass):
    def setUp(self):
        self.generalSetUp()
        self.navigationbar = NavigationBarClass(self.driver)

    def test_simpleTC(self):
        self.driver.get("https://www.apple.com")

    def tearDown(self):
        time.sleep(1)
        self.driver.close()
