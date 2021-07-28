import time

from locators import home_page_locators
from base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from locators import catalog_locators

class CatalogPage(BasePage):

    def add_product_in_stock_in_cart(self):
     self.find_element(catalog_locators.PRODUCT_IN_STOCK).click()

    def add_product_in_preorder_in_cart(self):
        self.find_element(catalog_locators.PRODUCT_IN_PREORDER).click()

    def go_to_basket(self):
       self.find_element(catalog_locators.ADD_PRODUCT_IN_CART).click()