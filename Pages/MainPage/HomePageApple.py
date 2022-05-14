from Locators.Locators import *
from Common.CustomFind.FindElement import FindElement


class NavigationBarClass():
    def __init__(self,driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)


    def click_mac_button(self):
        mac = self.findElement.find(*navigatinBarMac)
        mac.click()

    def click_ipad_button(self):
        ipad = self.findElement.find(*navigatinBarIpad)
        ipad.click()

    def click_iphone_button(self):
        iphone = self.findElement.find(*navigatinBarIphone)
        iphone.click()

    def click_watch_button(self):
        watch = self.findElement.find(*navigatinBarWatch)
        watch.click()

    def click_airpods_button(self):
        airpods = self.findElement.find(*navigatinBarAirPods)
        airpods.click()

    def click_tv_home_button(self):
        tvhome = self.findElement.find(*navigatinBarTVHome)
        tvhome.click()

    def click_only_on_apple_button(self):
        only = self.findElement.find(*navigatinBarOnlyOnApple)
        only.click()

    def click_where_to_buy_button(self):
        buy = self.findElement.find(*navigatinBarWhereToBuy)
        buy.click()


    def click_bag_button(self):
        bag = self.findElement.find(*navigatinBarBag)
        bag.click()

    def click_hidn_bag_button(self):
        hidnbag = self.findElement.find(*navigatinBarHidnBag)
        hidnbag.click()