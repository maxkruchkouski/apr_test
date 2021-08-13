from selenium.webdriver.common.by import By

BANNER = By.XPATH,"//body/apr-root[1]/apr-home[1]/apr-fw-banners[1]/div[1]/ngx-slick-carousel[1]/div[1]/div[1]/div[@class='slide slick-slide ng-star-inserted slick-current slick-active']"

#CATEGORY
def category_name(name):
    return (By.XPATH,f"//apr-header-main-nav/div[1]/div[1]/div[1]/ul[1]/li//*[text()='{name}']")

BANNER = By.XPATH,"//body/apr-root[1]/apr-home[1]/apr-fw-banners[1]/div[1]/ngx-slick-carousel[1]/div[1]/div[1]/div[@class='slide slick-slide ng-star-inserted slick-current slick-active']"
CATEGORY_MAC = By.XPATH,"//apr-header-main-nav/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]"
CATEGORY_IPAD = By.XPATH, "//apr-header-main-nav/div[1]/div[1]/div[1]/ul[1]/li[2]/a[1]"
CATEGORY_IPHONE = By.XPATH,"//apr-header-main-nav/div[1]/div[1]/div[1]/ul[1]/li[3]/a[1]"
CATEGORY_TV = By.XPATH,'//apr-header-main-nav/div[1]/div[1]/div[1]/ul[1]/li[4]/a[1]'
CATEGORY_AIRPODS = By.XPATH,"//apr-header-main-nav/div[1]/div[1]/div[1]/ul[1]/li[5]/a[1]"
CATEGORY_SMART_HOME = By.XPATH,"//a[contains(text(),'Умный дом')]"
CATEGORY_ACCESSORIES = By.XPATH,"//apr-header-main-nav/div[1]/div[1]/div[1]/ul[1]/li[7]/a[1]"
CATEGORY_BANG_AND_OLUFSEN = By.XPATH,"//apr-header-main-nav/div[1]/div[1]/div[1]/ul[1]/li[8]/a[1]"
PROMOTIONS = By.XPATH,"//apr-header-main-nav/div[1]/div[1]/div[1]/ul[2]/li[1]/a[1]"
SERVICE = By.XPATH,'//apr-header-main-nav/div[1]/div[1]/div[1]/ul[2]/li[2]/a[1]'
REVIEWS = By.XPATH,'//apr-header-main-nav/div[1]/div[1]/div[1]/ul[2]/li[3]/a[1]'

#SUBCATEGORY
SUBCATEGORY_MACBOOK_PRO = By.XPATH,'//apr-header-main-nav/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/ul[1]/li[1]/a[1]'
SUBCATEGORY_MACBOOK_AIR = By.XPATH,'//apr-header-main-nav/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/ul[1]/li[2]/a[1]'
SUBCATEGORY_MAC_MINI = By.XPATH,'//apr-header-main-nav/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/ul[1]/li[3]/a[1]'
SUBCATEGORY_I_MAC = By.XPATH,'//apr-header-main-nav/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/ul[1]/li[4]/a[1]'


PERSONAL_AREA = (By.XPATH,"//button[@class='btn btn-sign-in']")

COMPARE = By.XPATH,"//apr-header-main/nav[1]/div[1]/div[1]/div[1]/a[1]"
FAVORITES = By.XPATH,"//apr-header-main/nav[1]/div[1]/div[1]/div[2]/button[1]"
CART_BUTTON_HEADER = By.XPATH,'//apr-header-main/nav[1]/div[1]/div[1]/div[3]/a[1]'

SEARCH_BUTTON = By.XPATH,"//apr-header-main/nav[1]/div[1]/button[2]/*[1]"
INPUT_SEARCH_BUTTON = By.XPATH,"//apr-header-search-dropdown/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/input[1]"
TEXT_RESPONSE_SEARCH = By.XPATH,"//body/apr-root[1]/apr-search[1]/div[1]/div[1]/div[1]/div[1]/apr-search-info[1]/div[1]/p[1]"

HEADER_SITE_BANNER = By.XPATH,"//apr-header-site-banner/a[1]/div[1]/picture[1]/img[1]"

SENDPULSE = (By.XPATH,'//div[@class="sp-prompt sp-native-popover sp-pos-right show-prompt"]')
CLOSE_SENDPULSE = (By.XPATH, '//button[@class="sp-prompt-close"]')


