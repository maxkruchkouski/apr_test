from base_page import BasePage
from locators import cart_locators

class Cart(BasePage):

    def get_all_elements_in_cart(self):
       return self.find_element(cart_locators.ALL_ELEMENTS_IN_CART).text