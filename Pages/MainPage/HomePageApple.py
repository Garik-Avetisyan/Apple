from Locators.LocatorsFile import *
from Common.CustomFind.FindElement import FindElement
from Locators.Locators import * # for Tatevik


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
# <<<<<<< HEAD
# =======

class ChapterNavigationBarClass():
     def __init__(self, driver):
         self.driver = driver
         self.findElement = FindElement(self.driver)

     def click_macbook_air_button(self):
            macbookair = self.findElement.find(*chapternavBarMacBookAir)
            macbookair.click()

     def click_macbook_pro_button(self):
            macbookPro = self.findElement.find(*chapternavBarMacBookPro)
            macbookPro.click()

     def click_imac24_button(self):
            macbookPro = self.findElement.find(*chapternavBarMacBookPro)
            macbookPro.click()

     def click_mac_mini_button(self):
            macMini = self.findElement.find(*chapternavBarMacMini)
            macMini.click()

     def click_mac_studio_button(self):
            macStudio = self.findElement.find(*chapternavBarMacStudio)
            macStudio.click()

     def click_mac_pro_button(self):
            macPro = self.findElement.find(*chapternavBarMacPro)
            macPro.click()

     def click_mac_compare_button(self):
            macCompare = self.findElement.find(*chapternavBarMacCompare)
            macCompare.click()

     def click_displays_button(self):
            displays = self.findElement.find(*chapternavBarDisplays)
            displays.click()

     def click_accessories_button(self):
            accessories = self.findElement.find(*chapternavBarAccessories)
            accessories.click()

     def click_monterey_button(self):
            monterey = self.findElement.find(*chapternavBarMonterey)
            monterey.click()

     def click_shop_mac_button(self):
            shopMac = self.findElement.find(*chapternavShopMac)
            shopMac.click()

     def click_iphone_13_pro_button(self):
            iphone13Pro = self.findElement.find(*chapternavIphone13Pro)
            iphone13Pro.click()

     def click_iphone_13_button(self):
             iphone13 = self.findElement.find(*chapternavIphone13)
             iphone13.click()

     def click_iphone_se_button(self):
             iphoneSE = self.findElement.find(*chapternavIphoneSE)
             iphoneSE.click()

     def click_iphone_12_button(self):
            iphone12 = self.findElement.find(*chapternavIphone12)
            iphone12.click()

     def click_iphone_11_button(self):
            iphone11 = self.findElement.find(*chapternavIphone11)
            iphone11.click()

     def click_iphone_compare_button(self):
            iphoneConmpare = self.findElement.find(*chapternavBarIphoneCompare)
            iphoneConmpare.click()

     def click_airpods_button(self):
            airpods = self.findElement.find(*chapternavBarAirpods)
            airpods.click()

     def click_airtag_button(self):
            airTag = self.findElement.find(*chapternavBarAirTag)
            airTag.click()

     def click_iphone_accessories_button(self):
            iphoneAccessories = self.findElement.find(*chapternavBarIphoneAccessories)
            iphoneAccessories.click()

     def click_apple_card_button(self):
            appleCard = self.findElement.find(*chapternavBarAppleCard)
            appleCard.click()

     def click_shop_phone_button(self):
            shop_phone = self.findElement.find(*chapternavBarShopIphone)
            shop_phone.click()

     def click_apple_watch_s7_button(self):
             appleWatchS7 = self.findElement.find(*chapternavBarAppleWatchS7)
             appleWatchS7.click()

     def click_apple_watch_se_button(self):
             appleWatchSE = self.findElement.find(*chapternavBarAppleWatchSE)
             appleWatchSE.click()

     def click_apple_watch_s3_button(self):
             appleWatchS3 = self.findElement.find(*chapternavBarAppleWatchS3)
             appleWatchS3.click()

     def click_apple_watch_nike_button(self):
             appleWatchNike = self.findElement.find(*chapternavBarAppleWatchNike)
             appleWatchNike.click()

     def click_apple_watch_hermes_button(self):
             appleWatchHermes = self.findElement.find(*chapternavBarAppleWatchHermes)
             appleWatchHermes.click()

     def click_apple_watch_studio_button(self):
             appleWatchStudio = self.findElement.find(*chapternavBarAppleWatchStudio)
             appleWatchStudio.click()

     def click_apple_watch_compare_button(self):
             appleWatchCompare = self.findElement.find(*chapternavBarAppleWatchCompare)
             appleWatchCompare.click()

     def click_apple_watch_bands_button(self):
             appleWatchBands= self.findElement.find(*chapternavBarAppleWatchBands)
             appleWatchBands.click()

     def click_airpods_2nd_gen_button(self):
             airpods2ndGen= self.findElement.find(*chapternavBarAirpods2ndGen)
             airpods2ndGen.click()

     def click_airpods_pro_button(self):
            airpodsPro = self.findElement.find(*chapternavBarAirpodsPro)
            airpodsPro.click()

     def click_airpods_3rd_gen_button(self):
            airpords3rdGen = self.findElement.find(*chapternavBarAirpods3rdGen)
            airpords3rdGen.click()

     def click_airpods_max_button(self):
            airpordsMax = self.findElement.find(*chapternavBarAirpodsMax)
            airpordsMax.click()

     def click_airpods_compare_button(self):
            airpordsCompare = self.findElement.find(*chapternavBarAirpodsCompare)
            airpordsCompare.click()

     def click_apple_music_button(self):
            appleMusic = self.findElement.find(*chapternavBarAppleMusic)
            appleMusic.click()












# >>>>>>> ddb1dbf77fd24d97c2fa2e5a2bfbf557979b81ab
