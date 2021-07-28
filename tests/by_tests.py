import pytest

from pages.cart_page import Cart
from pages.home_page import HomePage
import time
from pages.catalog_page import CatalogPage
from pages.authorization_page import Authorization

def test_search_for_category(driver):
    driver.get("https://i-store.by")
    home_page = HomePage(driver)
    home_page.wait_send_pulse()
    home_page.close_sendpulse()
    home_page.click_search_button()
    home_page.enter_text_in_search_input()
    quantity_results_of_search = home_page.get_quantity_results_of_search_ru()
    assert  quantity_results_of_search != 0
    # home_page.open_category_mac()
    # home_page.open_category_ipad()
    # home_page.open_category_iphone()
    # home_page.open_category_tv()
    # home_page.open_category_airpods()
    # home_page.open_category_smart_home()
    # home_page.open_category_accessories()
    # home_page.open_category_bang_and_olufsen()
    # home_page.open_category_promotions()
    # home_page.open_category_service()
    # home_page.open_category_reviews()
    # home_page.click_search_button()
    # home_page.enter_text_in_search_input()
    # quantity_results_of_search = home_page.get_quantity_results_of_search()
    # assert  quantity_results_of_search != 0

    # breakpoint()

def test_authorization_with_phone_number(driver):
    driver.get("https://i-store.by")
    home_page = HomePage(driver)
    home_page.wait_send_pulse()
    home_page.close_sendpulse()
    name_button_before_login = home_page.get_name_personal_area()
    home_page.open_pop_up_privat_area()
    authorization_page = Authorization(driver)
    authorization_page.delete_symbols()
    authorization_page.enter_login_tel()
    authorization_page.click_proceed_button()
    authorization_page.enter_password_tel()
    authorization_page.click_proceed_button()
    name_button_after_login = home_page.get_name_personal_area()
    assert name_button_before_login != name_button_after_login

def test_authorization_with_e_mail(driver,):
    driver.get("https://i-store.by")
    home_page = HomePage(driver)
    home_page.wait_send_pulse()
    home_page.close_sendpulse()
    name_button_before_login = home_page.get_name_personal_area()
    home_page.open_pop_up_privat_area()
    authorization_page = Authorization(driver)
    authorization_page.delete_symbols()
    authorization_page.enter_login_e_mail()
    authorization_page.click_proceed_button()
    authorization_page.enter_password_e_mail()
    authorization_page.click_proceed_button()
    name_button_after_login = home_page.get_name_personal_area()
    assert name_button_before_login != name_button_after_login

def test_authorization_google_id(driver):
    driver.get("https://i-store.by")
    home_page = HomePage(driver)
    home_page.wait_send_pulse()
    home_page.close_sendpulse()
    name_button_before_login = home_page.get_name_personal_area()
    home_page.open_pop_up_privat_area()
    authorization_page = Authorization(driver)
    authorization_page.click_button_google_id()
    authorization_page.enter_login_google_id()
    authorization_page.click_button_proceed_in_google_id()
    authorization_page.enter_password_google_id()
    authorization_page.click_button_proceed_in_google_id()
    name_button_after_login = home_page.get_name_personal_area()
    assert name_button_before_login != name_button_after_login

# @pytest.mark.screenshot_on_failure
def test_authorization_facebook_id(driver):
    driver.get("https://i-store.by")
    # driver.save_screenshot("screenshot.png")
    home_page = HomePage(driver)
    home_page.wait_send_pulse()
    home_page.close_sendpulse()
    name_button_before_login = home_page.get_name_personal_area()
    home_page.open_pop_up_privat_area()
    authorization_page = Authorization(driver)
    authorization_page.click_button_facebook()
    authorization_page.enter_login_and_password_facebook()
    authorization_page.click_button_proceed_in_facebook()
    name_button_after_login = home_page.get_name_personal_area()
    assert name_button_before_login != name_button_after_login

def test_add_product_in_stock_in_cart(driver):
    driver.get("https://i-store.by")
    home_page = HomePage(driver)
    home_page.wait_send_pulse()
    home_page.close_sendpulse()
    home_page.move_to_category_mac()
    home_page.open_subcategory_macbook_pro()
    catalog_page =CatalogPage(driver)
    catalog_page.add_product_in_stock_in_cart()
    catalog_page.go_to_basket()
    cart_page = Cart(driver)
    all_products_in_cart = cart_page.get_all_elements_in_cart()
    assert all_products_in_cart != None
#
#
# def test_add_product_in_preorder_in_cart(driver):
#     site = SITES(driver)
#     site.go_to_site_by()
#     home_page = HomePage(driver)
#     home_page.wait_send_pulse()
#     home_page.close_sendpulse()
#     home_page.move_to_category("iPad")
#     home_page.open_subcategory("iPad Pro 12,9")
#     catalog_page =CatalogPage(driver)
#     catalog_page.add_product_in_preorder_in_cart()
#     catalog_page.go_to_basket()
#     cart_page = Cart(driver)
#     all_products_in_cart = cart_page.get_all_elements_in_cart()
#     assert all_products_in_cart != None