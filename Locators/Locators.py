from selenium.webdriver.common.by import By

# homePageCart = (By.ID, "nav-cart-count")
navigatinBarMac = (By.XPATH, "(//a[@href='/mac/'])[1]")
navigatinBarIpad = (By.XPATH, "(//a[@href='/ipad/'])[1]")
navigatinBarIphone = (By.XPATH, "(//a[@href='/iphone/'])[1]")
navigatinBarWatch = (By.XPATH, "(//a[@href='/watch/'])[1]")
navigatinBarAirPods = (By.XPATH, "(//a[@href='/airpods/'])[1]")
navigatinBarTVHome = (By.XPATH, "(//a[@href='/tv-home/'])[1]")
navigatinBarOnlyOnApple = (By.XPATH, "(//a[@href='/services/'])[1]")
navigatinBarWhereToBuy = (By.XPATH, "(//a[@href='/buy/'])[1]")

navigatinBarBag = (By.XPATH, "//span[@class='ac-gn-bag-badge-unit']")
navigatinBarHidnBag = (By.CLASS_NAME, "ac-gn-bagview-nav-link ac-gn-bagview-nav-link-bag")

# homePageChapterNav
chapternavBarMacBookAir = (By.XPATH, "(//a[@href='/macbook-air/'])")
chapternavBarMacBookPro = (By.XPATH, "(//a[@href='/macbook-pro/'])")
chapternavBarImac24 = (By.XPATH, "(//a[@href='/imac-24/'])")
chapternavBarMacMini = (By.XPATH, "(//a[@href='/mac-mini/'])")
chapternavBarMacStudio = (By.XPATH, "(//a[@href='/mac -studio/'])")
chapternavBarMacPro = (By.XPATH, "(//a[@href='/mac-pro/'])")
chapternavBarMacCompare = (By.XPATH, "(//a[@href='/mac/compare/'])")
chapternavBarDisplays = (By.XPATH, "(//a[@href='/displays/'])")
chapternavBarAccessories = (By.XPATH, "(//a[@href='/us/shop/goto/mac/accessories'])")
chapternavBarMonterey = (By.XPATH, "(//a[@href='/macos/monterey/'])")
chapternavShopMac = (By.XPATH, "(//a[@href='/us/shop/goto/buy_mac'])")
chapternavIphone13Pro = (By.XPATH, "(//a[@href='/iphone-13-pro/'])")
chapternavIphone13 = (By.XPATH, "(//a[@href='/iphone-13/'])")
chapternavIphoneSE = (By.XPATH, "(//a[@href='/iphone-se/'])")
chapternavIphone12 = (By.XPATH, "(//a[@href='/iphone-12/key-features/'])")
chapternavIphone11 = (By.XPATH, "(//a[@href='/us/shop/goto/buy_iphone/iphone_11'])")
chapternavBarIphoneCompare = (By.XPATH, "(//a[@href='/iphone/compare/'])")
chapternavBarAirpods = (By.XPATH, "(//a[@href='/airpods/'])")
chapternavBarAirTag = (By.XPATH, "(//a[@href='/airtag/'])")
chapternavBarIphoneAccessories = (By.XPATH, "(//a[@href='/us/shop/goto/iphone/accessories'])")
chapternavBarAppleCard = (By.XPATH, "(//a[@href='/apple-card/'])")
chapternavBariOS15 = (By.XPATH, "(//a[@href='/ios/ios-15/'])")
chapternavBarShopIphone = (By.XPATH, "(//a[@href='/us/shop/goto/iphone/accessories'])")
chapternavBarAppleWatchS7 = (By.XPATH, "(//a[@href='/apple-watch-series-7/'])")
chapternavBarAppleWatchSE = (By.XPATH, "(//a[@href='/apple-watch-se/'])")
chapternavBarAppleWatchS3 = (By.XPATH, "(//a[@href='/apple-watch-series-3/'])")
chapternavBarAppleWatchNike = (By.XPATH, "(//a[@href='/apple-watch-nike/'])")
chapternavBarAppleWatchHermes = (By.XPATH, "(//a[@href='/apple-watch-hermes/'])")
chapternavBarAppleWatchStudio = (By.XPATH, "(//a[@href='/us/shop/goto/studio/apple_watch'])")
chapternavBarAppleWatchCompare = (By.XPATH, "(//a[@href='/watch/compare/'])")
chapternavBarAppleWatchBands = (By.XPATH, "(//a[@href='/us/shop/goto/watch/bands'])")
chapternavBarAirpods2ndGen = (By.XPATH, "(//a[@href='/airpods-2nd-generation/'])")
chapternavBarAirpodsPro = (By.XPATH, "(//a[@href='/airpods-pro/'])")
chapternavBarAirpods3rdGen = (By.XPATH,"(//a[@href='/airpods-3rd-generation/'])")
chapternavBarAirpodsMax = (By.XPATH, "(//a[@href='/airpods-max/'])")
chapternavBarAirpodsCompare = (By.XPATH, "(//a[@href='/airpods/compare/'])")
chapternavBarAppleMusic = (By.XPATH, "(//a[@href='/apple-music/'])")

# <<<<<<< HEAD

#SelectProductDetailsPage

blackColor = (By.XPATH, "(//div[@class ='rc-dimension-multiple form-selector-swatch column large-6 small-6 form-selector'])[5]")
gb64 = (By.XPATH, "(//div[@class ='rc-dimension-multiple form-selector-threeline column large-6 small-6 form-selector'])[1]")
connectLoc = (By.XPATH, "(//div[@class ='rf-dimension-simfree rc-dimension-multiple form-selector-threeline column large-12 small-12 form-selector'])[1]")
pressNO = (By.ID, "noTradeIn")
oneTimePayment = (By.XPATH, "(//div[@class ='rc-dimension-selector-row form-selector-twocol-threeline form-selector'])[2]")
addBag = (By.NAME, "add-to-cart")
# =======


#Cart Section

cartSectionDeleteButtonLocator = (By.XPATH, "(//input[@class ='rs-iteminfo-remove as-buttonlink'])[1]")
cartSectionDeleteButtonLocatorAll = (By.XPATH, "//input[@class ='rs-iteminfo-remove as-buttonlink']")
# >>>>>>> c293a61f22f68d644df60b0e273261881b265562


#Locators Meri

buyBtn = (By.LINK_TEXT, "Buy")

#WatchListPage
firstWatchLocator = (By.XPATH, "(//div[@class='rf-wuipselect-wuip rf-wuipselect-wuip-rollover-hover'])[1]")

#WatchDetailsPage
watchColorLocator = (By.XPATH, "(//img[@class='colornav-swatch'])[4]")
caseSizeLocator = (By.XPATH, "(//label[@class='form-selector-label'])[2]")
gpsOrGpsCellularLocator = (By.XPATH, "(//label[@class='form-selector-label'])[4]")
bagButtonLocator = (By.XPATH, "//button[@class='button button-block']")

# Accessories Page Locators
accessoriesPageSearchFieldLocator = (By.XPATH, "//input[@name='search']")

# Product Details Page Locators
productDetailsPageColorImageLocator = (By.XPATH, "(//img[@class='colornav-swatch'])[1]")
productDetailsPageAddToBagButtonLocator = (By.ID, "add-to-cart")

#Search Results Page Locators
searchResultsPageFirstProductLocator = (By.XPATH, "(//img[@class='rc-inline-gallery-image'])[1]")