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

#Cart Section

cartSectionDeleteButtonLocator = (By.XPATH, "(//input[@class ='rs-iteminfo-remove as-buttonlink'])[1]")
cartSectionDeleteButtonLocatorAll = (By.XPATH, "//input[@class ='rs-iteminfo-remove as-buttonlink']")