from selenium.webdriver.common.by import By

PRODUCT_IN_STOCK = (By.XPATH,'//body/apr-root[1]/apr-catalog-subcategory[1]/div[1]/div[1]/div[1]/div[2]/apr-catalog-list[1]/div[1]/div[1]/div[2]/apr-catalog-list-item[1]/div[1]/div[4]/div[2]/div[3]/apr-product-order-button[1]/div[1]/apr-base-button[1]/button[1]')
PRODUCT_IN_PREORDER = (By.XPATH,'//body/apr-root[1]/apr-catalog-subcategory[1]/div[1]/div[1]/div[1]/div[2]/apr-catalog-list[1]/div[1]/div[1]/div[1]/apr-catalog-list-item[1]/div[1]/div[4]/div[2]/div[3]/apr-product-order-button[1]/div[1]/apr-base-button[1]/button[1]')
ADD_PRODUCT_IN_CART = (By.XPATH,'/html[1]/body[1]/div[2]/div[2]/div[1]/mat-dialog-container[1]/apr-add-to-cart-modal[1]/div[1]/div[4]/apr-base-button[1]/button[1]')