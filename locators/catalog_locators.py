from selenium.webdriver.common.by import By

PRODUCT_IN_STOCK = (By.XPATH,'(//button[@class="btn btn-base"])')
PRODUCT_IN_PREORDER = (By.XPATH,'(//button[@class="btn btn-base btn-yellow"])')
ADD_PRODUCT_IN_CART = (By.XPATH,"//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/apr-add-to-cart-modal[1]/div[1]/div[5]/apr-base-button[1]")
BUTTON_BUY_TOGETHER = (By.XPATH,'//body/div[2]/div[2]/div[1]/mat-dialog-container[1]/apr-add-to-cart-modal[1]/div[1]/div[3]/apr-product-bundles[1]/div[1]/div[1]/div[1]/ngx-slick-carousel[1]/div[1]/div[1]/div[2]/apr-bundle-result[1]/div[2]/apr-base-button[1]/button[1]')
PRODUCT_NAME_AND_SKU= (By.XPATH,'//div[@class="product-item-info"]')
PRODUCT_COST = (By.XPATH,'//div[@class="product-item-prices"]')
PRODUCT_COST_FOR_GE = (By.XPATH,'//body/div[3]/div[2]/div[1]/mat-dialog-container[1]/apr-add-to-cart-modal[1]/div[1]/div[1]/apr-product-item[1]/div[1]/div[2]/div[2]/p[1]')
PRODUCT_NAME_AND_SKU_FOR_GE = (By.XPATH,'//body/div[3]/div[2]/div[1]/mat-dialog-container[1]/apr-add-to-cart-modal[1]/div[1]/div[1]/apr-product-item[1]/div[1]/div[2]/div[1]')
ADD_PRODUCT_IN_CART_FOR_GE = (By.XPATH,'(//button[@class="btn btn-base"])[8]')
PRODUCT_IN_CATALOG = By.XPATH, '//body/apr-root[1]/apr-catalog-subcategory[1]/div[1]/div[1]/div[1]/div[2]/apr-catalog-list[1]/div[1]/div[1]/div[1]/apr-catalog-list-item[1]/div[1]/div[3]'
BUTTON_ORDER_IN_ONE_CLICK = By.XPATH, '//div[@class="card-one-click-order btn ng-star-inserted"]/div[1]'
INPUT_YOUR_NAME_FOR_ORDER_ONE_CLICK = By.XPATH,"//input[@id='o-c-f-name']"
INPUT_PHONE_NUMBER_FOR_ORDER_ONE_CLICK = (By.XPATH,"//input[@id='phone']")
BUTTON_WAITING_FOR_A_CALL = By.XPATH,'//button[@class="btn btn-brand-blue float-right"]'
TOAST_AFTER_ORDER_IN_ONE_CLICK = By.XPATH,"//div[@id='toast-container']"