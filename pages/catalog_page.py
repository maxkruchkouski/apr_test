import time

from locators import home_page_locators
from base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from locators import catalog_locators

class CatalogPage(BasePage):

    def add_product_in_stock_in_cart(self):
     self.waits_clickable_element(catalog_locators.PRODUCT_IN_STOCK).click()

    def add_product_in_preorder_in_cart(self):
        self.waits_clickable_element(catalog_locators.PRODUCT_IN_PREORDER).click()

    def go_to_basket(self):
        elem = self.find_element(catalog_locators.ADD_PRODUCT_IN_CART)
        self.move_to_element(elem)
        self.waits_clickable_element(catalog_locators.ADD_PRODUCT_IN_CART).click()

    def go_to_basket_for_ge(self):
        elem = self.find_element(catalog_locators.ADD_PRODUCT_IN_CART_FOR_GE)
        self.move_to_element(elem)
        self.waits_clickable_element(catalog_locators.ADD_PRODUCT_IN_CART_FOR_GE).click()

    def click_button_buy_together_for_bundles(self):
        self.waits_clickable_element(catalog_locators.BUTTON_BUY_TOGETHER).click()

    def get_product_name_and_sku_in_pop_up(self):
        return self.find_element(catalog_locators.PRODUCT_NAME_AND_SKU).text

    def get_product_name_and_sku_in_pop_up_for_ge(self):
        return self.find_element(catalog_locators.PRODUCT_NAME_AND_SKU_FOR_GE).text

    def get_product_cost_in_pop_up(self):
        return self.find_element(catalog_locators.PRODUCT_COST).text

    def get_product_cost_in_pop_up_for_ge(self):
        return self.find_element(catalog_locators.PRODUCT_COST_FOR_GE).text

    def open_product_in_catalog(self):
        time.sleep(1)
        self.waits_clickable_element(catalog_locators.PRODUCT_IN_CATALOG).click()

    def click_button_order_in_one_click(self):
        elem = self.find_element(catalog_locators.BUTTON_ORDER_IN_ONE_CLICK)
        self.move_to_element(elem)
        time.sleep(1)
        self.waits_clickable_element(catalog_locators.BUTTON_ORDER_IN_ONE_CLICK).click()

    def enter_name_for_order_in_one_click(self):
        elem = self.find_element(catalog_locators.INPUT_YOUR_NAME_FOR_ORDER_ONE_CLICK).click()
        self.find_element(catalog_locators.INPUT_YOUR_NAME_FOR_ORDER_ONE_CLICK).send_keys("test")

    def enter_phone_number_for_order_in_one_click(self):
        self.find_element(catalog_locators.INPUT_PHONE_NUMBER_FOR_ORDER_ONE_CLICK).send_keys('+375291234567')

    def click_button_waiting_for_a_call_for_order_in_one_click(self):
        self.waits_clickable_element(catalog_locators.BUTTON_WAITING_FOR_A_CALL).click()

    def get_text_from_toast_after_order_in_one_click(self):
        time.sleep(1)
        return self.find_element(catalog_locators.TOAST_AFTER_ORDER_IN_ONE_CLICK).text
