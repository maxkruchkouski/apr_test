from locators import checkout_locators
from base_page import BasePage

class CheckoutPage(BasePage):

    def enter_name_on_checkout_page(self):
        self.find_element(checkout_locators.INPUT_YOUR_NAME).send_keys('test')

    def enter_phone_number_on_checkout_page(self):
        self.find_element(checkout_locators.INPUN_YOUR_PHONE_NUMBER).send_keys('+375291234567')

    def enter_email_on_checkout_page(self):
        self.find_element(checkout_locators.INPUT_YOUR_EMAIL).send_keys('test@test.com')

    def send_comment(self):
        self.find_element(checkout_locators.INPUT_COMMENT).send_keys('test')



    #choice of delivery method

    def click_button_delivery_in_minsk(self):
        self.waits_clickable_element(checkout_locators.DELIVERY_IN_MINSK).click()

    def click_button_delivery_across_belarus(self):
        self.waits_clickable_element(checkout_locators.DELIVERY_ACROSS_BELARUS).click()

    def click_button_pick_up_from_the_branch(self):
        self.waits_clickable_element(checkout_locators.PICK_UP_FROM_THE_BRANCH).click()