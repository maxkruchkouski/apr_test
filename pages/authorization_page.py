from base_page import BasePage
from locators import authorization_locators
from locators import home_page_locators
import time
# from base_page import text_to_change

class Authorization(BasePage):

    def get_name_personal_area(self):
        # time.sleep(4.5)
        return self.find_element(home_page_locators.PERSONAL_AREA).text

    def enter_login_tel(self):
        self.find_element(authorization_locators.INPUT_LOGIN_PERSONAL_AREA).send_keys('+375293992761')

    def delete_symbols(self):
        self.delete_with_js(authorization_locators.INPUT_LOGIN_PERSONAL_AREA, 4)

    def click_proceed_button(self):
        self.find_element(authorization_locators.BUTTON_PROCEED_IN_PERSONAL_AREA).click()

    def enter_password_tel(self):
        self.find_element(authorization_locators.INPUT_PASSWORD_PERSONAL_AREA).send_keys("123123123")

    def enter_login_e_mail(self):
        self.find_element(authorization_locators.INPUT_LOGIN_PERSONAL_AREA).send_keys('bullet-max@mail.ru')

    def enter_password_e_mail(self):
        self.find_element(authorization_locators.INPUT_PASSWORD_PERSONAL_AREA).send_keys("123123123")

    def click_button_google_id(self):
        time.sleep(1)
        self.find_element(authorization_locators.BUTTON_GOOGLE_ID).click()

    def enter_login_google_id(self):
        self.find_element(authorization_locators.INPUT_LOGIN_GOOGLE_ID).send_keys("apr_test@mail.ru")

    def click_button_proceed_in_google_id(self):
        self.find_element(authorization_locators.BUTTON_PROCEED_IN_SOCIAL_NETWORK).click()

    def enter_password_google_id(self):
        time.sleep(2)
        self.find_element(authorization_locators.INPUT_PASSWORD_GOOGLE_ID).send_keys('apr_test_123123123')

    def click_button_facebook(self):
        time.sleep(1)
        self.find_element(authorization_locators.BUTTON_FACEBOOK).click()

    def enter_login_and_password_facebook(self):
        self.find_element(authorization_locators.INPUT_LOGIN_FACEBOOK).send_keys("+375293992761")
        self.find_element(authorization_locators.INPUT_PASSWORD_FACEBOOK).send_keys('3992761000')

    def click_button_proceed_in_facebook(self):
        self.find_element(authorization_locators.BUTTON_PROCEED_FACEBOOK).click()




