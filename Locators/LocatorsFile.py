from selenium.webdriver.common.by import By

#for validation
validation = (By.XPATH,"(//span[@class='chapternav-label'])[1]")
validation_access = (By.XPATH,"//span[@class='disclosure-text']")

#Garik locators
navigatinBarMac = (By.XPATH, "//li[@class='ac-gn-item ac-gn-item-menu ac-gn-mac']")
navigatinBarIpad = (By.XPATH, "//li[@class='ac-gn-item ac-gn-item-menu ac-gn-ipad']")
navigatinBarIphone = (By.XPATH, "//li[@class='ac-gn-item ac-gn-item-menu ac-gn-iphone']")
navigatinBarWatch = (By.XPATH, "//li[@class='ac-gn-item ac-gn-item-menu ac-gn-watch']")
navigatinBarAirPods = (By.XPATH, "//li[@class='ac-gn-item ac-gn-item-menu ac-gn-airpods']")
navigatinBarTVHome = (By.XPATH, "//li[@class='ac-gn-item ac-gn-item-menu ac-gn-tvhome']")
navigatinBarOnlyOnApple = (By.XPATH, "//li[@class='ac-gn-item ac-gn-item-menu ac-gn-onlyonapple']")
# navigatinBarWhereToBuy = (By.XPATH, "(//a[@href='/buy/'])[1]") #?
navigatinBarAccessories = (By.XPATH, "//li[@class='ac-gn-item ac-gn-item-menu ac-gn-accessories']")
#Tamara locators
navigatinBarBag = (By.XPATH, "ac-gn-bag-badge-unit")
navigatinBarHidnBag = (By.XPATH, "//a[@href='https://www.apple.com/shop/bag']")

# <<<<<<< HEAD

#SelectProductDetailsPage

blackColor = (By.XPATH, "(//div[@class ='rc-dimension-multiple form-selector-swatch column large-6 small-6 form-selector'])[5]")
gb64 = (By.XPATH, "(//div[@class ='rc-dimension-multiple form-selector-threeline column large-6 small-6 form-selector'])[1]")
connectLoc = (By.XPATH, "(//div[@class ='rf-dimension-simfree rc-dimension-multiple form-selector-threeline column large-12 small-12 form-selector'])[1]")
pressNO = (By.ID, "noTradeIn_label")
oneTimePayment = (By.XPATH, "(//div[@class ='rc-dimension-selector-row form-selector-twocol-threeline form-selector'])[2]")
addBag = (By.NAME, "add-to-cart")
# =======


# Cart Section

cartSectionDeleteButtonLocator = (By.XPATH, "(//input[@class ='rs-iteminfo-remove as-buttonlink'])[1]")
cartSectionDeleteButtonLocatorAll = (By.XPATH, "//input[@class ='rs-iteminfo-remove as-buttonlink']")
# >>>>>>> c293a61f22f68d644df60b0e273261881b265562


#Locators Meri

buyBtn = (By.LINK_TEXT, "Buy")
