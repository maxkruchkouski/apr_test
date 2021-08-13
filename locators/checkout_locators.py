from selenium.webdriver.common.by import By

#CUSTOMER
INPUT_YOUR_NAME = By.XPATH,'//mat-tab-body/div[1]/div[1]/apr-cart-checkout-form[1]/div[1]/form[1]/tabset[1]/div[1]/tab[1]/div[2]/div[1]/div[1]/apr-checkout-user-info[1]/div[1]/input[1]'
INPUN_YOUR_PHONE_NUMBER = By.XPATH, '//mat-tab-body/div[1]/div[1]/apr-cart-checkout-form[1]/div[1]/form[1]/tabset[1]/div[1]/tab[1]/div[2]/div[1]/div[1]/apr-checkout-user-info[1]/div[2]/div[1]/input[1]'
INPUT_YOUR_EMAIL = By.XPATH, '//mat-tab-body/div[1]/div[1]/apr-cart-checkout-form[1]/div[1]/form[1]/tabset[1]/div[1]/tab[1]/div[2]/div[1]/div[1]/apr-checkout-user-info[1]/div[3]/input[1]'
INPUT_COMMENT = By.XPATH, '//mat-tab-body/div[1]/div[1]/apr-cart-checkout-form[1]/div[1]/form[1]/tabset[1]/div[1]/tab[1]/div[2]/div[1]/div[1]/apr-checkout-user-info[1]/div[4]/textarea[1]'

#DELIVERY
DELIVERY_IN_MINSK = By.XPATH,'//mat-tab-body/div[1]/div[1]/apr-cart-checkout-form[1]/div[1]/form[1]/tabset[1]/div[1]/tab[1]/div[4]/div[1]/div[1]/div[1]/apr-checkout-delivery[1]/div[1]/div[1]/mat-radio-group[1]/mat-radio-button[1]/label[1]'
DELIVERY_ACROSS_BELARUS = By.XPATH,'//mat-tab-body/div[1]/div[1]/apr-cart-checkout-form[1]/div[1]/form[1]/tabset[1]/div[1]/tab[1]/div[4]/div[1]/div[1]/div[1]/apr-checkout-delivery[1]/div[1]/div[1]/mat-radio-group[1]/mat-radio-button[2]/label[1]'
PICK_UP_FROM_THE_BRANCH = By.XPATH,'//mat-tab-body/div[1]/div[1]/apr-cart-checkout-form[1]/div[1]/form[1]/tabset[1]/div[1]/tab[1]/div[4]/div[1]/div[1]/div[1]/apr-checkout-delivery[1]/div[1]/div[1]/mat-radio-group[1]/mat-radio-button[3]/label[1]'

#STORES
STORE_LENINA = By.XPATH,'//mat-tab-body/div[1]/div[1]/apr-cart-checkout-form[1]/div[1]/form[1]/tabset[1]/div[1]/tab[1]/div[4]/div[1]/div[1]/div[1]/apr-checkout-delivery[1]/div[1]/div[1]/div[1]/mat-radio-group[1]/mat-radio-button[1]/label[1]'
STORE_GREEN_CITY = By.XPATH,'//mat-tab-body/div[1]/div[1]/apr-cart-checkout-form[1]/div[1]/form[1]/tabset[1]/div[1]/tab[1]/div[4]/div[1]/div[1]/div[1]/apr-checkout-delivery[1]/div[1]/div[1]/div[1]/mat-radio-group[1]/mat-radio-button[2]/label[1]'
STORE_DANA_MALL = By.XPATH,'//mat-tab-body/div[1]/div[1]/apr-cart-checkout-form[1]/div[1]/form[1]/tabset[1]/div[1]/tab[1]/div[4]/div[1]/div[1]/div[1]/apr-checkout-delivery[1]/div[1]/div[1]/div[1]/mat-radio-group[1]/mat-radio-button[3]/label[1]'



#PAYMENT