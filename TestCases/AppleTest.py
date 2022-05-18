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




    def tearDown(self):
        time.sleep(3)
        self.driver.close()
