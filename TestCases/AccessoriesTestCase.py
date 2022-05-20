import time
import unittest
from selenium import webdriver
from Pages.AccessoriesPage.AccessoriesPage import AccessoriesPageClass
from Pages.AccessoriesPage.AccessoriesProductDetailsPage import ProductDetailsPageClass
from Pages.AccessoriesPage.AccessoriesSearchResultsPage import SearchResultsPageClass
from Pages.MainPage.HomePageApple import NavigationBarClass

class SelectAccessoriesTestClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../Common/Driver/chromedriver.exe")
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.accessoriesPage = AccessoriesPageClass(self.driver)
        self.productDetailsPage = ProductDetailsPageClass(self.driver)
        self.searchResultsPage = SearchResultsPageClass(self.driver)
        self.navigationBar = NavigationBarClass(self.driver)

    def test_accessories_TC(self):
        self.driver.get("https://www.apple.com/")
        self.navigationBar.click_accessories_button()
        self.accessoriesPage.fill_search_field("Iphone 13 case")
        self.searchResultsPage.click_on_first_product()
        self.productDetailsPage.click_on_color_image()
        self.productDetailsPage.click_on_add_to_bug_button()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()


