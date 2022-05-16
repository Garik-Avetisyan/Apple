from Locators.LocatorsFile import *
from Common.CustomFind.FindElement import FindElement


class NavigationBarClass():
    def __init__(self,driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)


    def click_mac_button(self):
        mac = self.findElement.find(*navigatinBarMac)
        mac.click()
        # validation block
        valid_text = self.findElement.find(*validation).text
        if "Mac" in valid_text:
            print(valid_text ," ok")
        else:
            print("Error : ",valid_text)
            exit("ERROR-1:")

    def click_ipad_button(self):
        ipad = self.findElement.find(*navigatinBarIpad)
        ipad.click()
        #validation block
        valid_text = self.findElement.find(*validation).text
        if "iPad" in valid_text:
            print(valid_text, " ok")
        else:
            print("Error : ", valid_text)
            exit("ERROR-1:")

    def click_iphone_button(self):
        iphone = self.findElement.find(*navigatinBarIphone)
        iphone.click()
        #validation block
        valid_text = self.findElement.find(*validation).text
        if "iPhone" in valid_text:
            print(valid_text, " ok")
        else:
            print("Error : ", valid_text)
            exit("ERROR-1:")

    def click_watch_button(self):
        watch = self.findElement.find(*navigatinBarWatch)
        watch.click()
        #validation block
        valid_text = self.findElement.find(*validation).text
        if "Watch" in valid_text:
            print(valid_text, " ok")
        else:
            print("Error : ", valid_text)
            exit("ERROR-1:")

    def click_airpods_button(self):
        airpods = self.findElement.find(*navigatinBarAirPods)
        airpods.click()
        #validation block
        valid_text = self.findElement.find(*validation).text
        if "AirPods" in valid_text:
            print(valid_text , " ok")
        else:
            print("Error : ", valid_text)
            exit("ERROR-1:")

    def click_tv_home_button(self):
        tvhome = self.findElement.find(*navigatinBarTVHome)
        tvhome.click()
        #validation block
        valid_text = self.findElement.find(*validation).text
        if "TV" in valid_text:
            print(valid_text, " ok")
        else:
            print("Error : ", valid_text)
            exit("ERROR-1:")

    def click_only_on_apple_button(self):
        only = self.findElement.find(*navigatinBarOnlyOnApple)
        only.click()
        #validation block
        valid_text = self.findElement.find(*validation).text
        if "TV+" in valid_text:
            print(valid_text, " ok")
        else:
            print("Error : ", valid_text)
            exit("ERROR-1:")

    def click_accessories_button(self):
        accessories = self.findElement.find(*navigatinBarAccessories)
        accessories.click()
        #validation block
        valid_text = self.findElement.find(*validation_access).text
        if "Browse" in valid_text:
            print(valid_text, " ok")
        else:
            print("Error : ", valid_text)
            exit("ERROR-1:")

    def click_where_to_buy_button(self):
        buy = self.findElement.find(*navigatinBarWhereToBuy)
        buy.click()

    def click_bag_button(self):
        bag = self.findElement.find(*navigatinBarBag)
        bag.click()

    def click_hidn_bag_button(self):
        hidnbag = self.findElement.find(*navigatinBarHidnBag)
        hidnbag.click()
