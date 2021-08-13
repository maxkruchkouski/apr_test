from selenium.webdriver.common.by import By
# ALL_ELEMENTS_IN_CART = (By.XPATH,'//div[@class="cart-step-content-wrapper ng-star-inserted"]')
ALL_ELEMENTS_IN_CART = (By.XPATH,'//div[@class="mat-tab-body-wrapper"]')
CARD_TOTAL_COST = By.XPATH,'//mat-tab-body/div[1]/div[1]/div[1]/div[1]/div[1]/apr-cart-promocode[1]/div[1]/div[4]/div[2]/div[1]'
OPEN_PROMO_CODE = (By.XPATH,'//mat-tab-body/div[1]/div[1]/div[1]/div[1]/div[1]/apr-cart-promocode[1]/div[1]/div[2]/div[1]')
INPUT_PROMO_CODE = (By.XPATH,'//mat-tab-body/div[1]/div[1]/div[1]/div[1]/div[1]/apr-cart-promocode[1]/div[1]/div[3]/form[1]/div[1]/div[1]/input[1]')
BUTTON_PROCEED_PROMO_CODE = (By.XPATH,'//mat-tab-body/div[1]/div[1]/div[1]/div[1]/div[1]/apr-cart-promocode[1]/div[1]/div[3]/form[1]/div[1]/div[2]/button[1]')
BUTTON_SUBMIT_ORDER = By.XPATH, '//mat-tab-body/div[1]/div[1]/div[1]/div[3]/div[2]/button[1]'