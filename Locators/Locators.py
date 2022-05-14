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

navigatinBarBag = (By.XPATH, "(//a[@class='ac-gn-link ac-gn-link-bag'])[2]")
navigatinBarHidnBag = (By.CLASS_NAME, "ac-gn-bagview-nav-link ac-gn-bagview-nav-link-bag")

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
