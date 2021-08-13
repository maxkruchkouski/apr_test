import time

from base_page import BasePage
from locators import cart_locators

class Cart(BasePage):

    def get_all_elements_in_cart(self):
       time.sleep(1)
       return self.find_element(cart_locators.ALL_ELEMENTS_IN_CART).text

    def get_total_cost_in_cart(self):
        return self.find_element(cart_locators.CARD_TOTAL_COST).text

    def open_input_promo_code(self):
        self.waits_clickable_element(cart_locators.OPEN_PROMO_CODE).click()

    def enter_promo_code(self):
        self.find_element(cart_locators.INPUT_PROMO_CODE).send_keys('123')

    def click_proceed_promo_code(self):
        self.waits_clickable_element(cart_locators.BUTTON_PROCEED_PROMO_CODE).click()

    def click_button_submit_order(self):
        self.waits_clickable_element(cart_locators.BUTTON_SUBMIT_ORDER).click()