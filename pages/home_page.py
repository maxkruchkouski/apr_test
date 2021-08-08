import time

from locators import home_page_locators
from base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class HomePage(BasePage):

    def scrolling_banners(self):
        a=self.find_element(home_page_locators.BANNER).get_attribute('data-slick-index')
        return a


    def wait_send_pulse(self):
        self.find_element(home_page_locators.SENDPULSE)

    def close_sendpulse(self):
        self.waits_clickable_element(home_page_locators.CLOSE_SENDPULSE).click()

    def open_category_mac(self):
        self.find_element(home_page_locators.CATEGORY_MAC).click()

    def open_category_ipad(self):
        self.find_element(home_page_locators.CATEGORY_IPAD).click()

    def open_category_iphone(self):
        self.find_element(home_page_locators.CATEGORY_IPHONE).click()

    def open_category_tv(self):
        self.find_element(home_page_locators.CATEGORY_TV).click()

    def open_category_airpods(self):
        self.find_element(home_page_locators.CATEGORY_AIRPODS).click()

    def open_category_smart_home(self):
        self.find_element(home_page_locators.CATEGORY_SMART_HOME).click()

    def open_category_accessories(self):
        self.find_element(home_page_locators.CATEGORY_ACCESSORIES).click()

    def open_category_bang_and_olufsen(self):
        self.find_element(home_page_locators.CATEGORY_BANG_AND_OLUFSEN).click()

    def open_category_promotions(self):
        self.find_element(home_page_locators.PROMOTIONS).click()

    def open_category_service(self):
        self.find_element(home_page_locators.SERVICE).click()

    def open_category_reviews(self):
        self.find_element(home_page_locators.REVIEWS).click()

    def click_search_button(self):
        self.find_element(home_page_locators.SEARCH_BUTTON).click()

    def enter_text_in_search_input(self):
        elem = self.find_element(home_page_locators.INPUT_SEARCH_BUTTON)
        elem.send_keys("iPhone 12")
        elem.send_keys(Keys.ENTER)
        time.sleep(4)

    def get_quantity_results_of_search_ru(self):
        elem = self.find_element(home_page_locators.TEXT_RESPONSE_SEARCH).text
        return (int(elem.split('найдено ')[1]))

    def get_quantity_results_of_search_az(self):
        elem = self.find_element(home_page_locators.TEXT_RESPONSE_SEARCH).text
        return (int(elem.split('Tapıldı ')[1]))

    def open_pop_up_privat_area(self):
        self.find_element(home_page_locators.PERSONAL_AREA).click()

    def get_name_personal_area(self):
        time.sleep(4.5)
        return self.find_element(home_page_locators.PERSONAL_AREA).text

    def open_subcategory_macbook_pro(self):
        self.find_element(home_page_locators.SUBCATEGORY_MACBOOK_PRO).click()

    def move_to_category_mac(self):
        elem = self.find_element(home_page_locators.CATEGORY_MAC)
        self.move_to_element(elem)

    def move_to_category_ipad(self):
        elem = self.find_element(home_page_locators.CATEGORY_IPAD)
        self.move_to_element(elem)

    def move_to_category_iphone(self):
        elem = self.find_element(home_page_locators.CATEGORY_IPHONE)
        self.move_to_element(elem)

    def move_to_category_tv(self):
        elem = self.find_element(home_page_locators.CATEGORY_TV)
        self.move_to_element(elem)

    def move_to_category_accessories(self):
        elem = self.find_element(home_page_locators.CATEGORY_ACCESSORIES)
        self.move_to_element(elem)

    def move_to_category_bang_and_olufsen(self):
        elem = self.find_element(home_page_locators.CATEGORY_BANG_AND_OLUFSEN)
        self.move_to_element(elem)

    def move_to_category_promotions(self):
        elem = self.find_element(home_page_locators.PROMOTIONS)
        self.move_to_element(elem)

    def move_to_category_service(self):
        elem = self.find_element(home_page_locators.SERVICE)
        self.move_to_element(elem)

    def move_to_category_reviews(self):
        elem = self.find_element(home_page_locators.REVIEWS)
        self.move_to_element(elem)