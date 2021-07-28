from pages.cart_page import Cart
from pages.home_page import HomePage
import time

from pages.catalog_page import CatalogPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_search_for_category(driver):
    driver.get("https://ispace.ge/")
    home_page = HomePage(driver)
    home_page.click_search_button()
    home_page.enter_text_in_search_input()
    quantity_results_of_search = home_page.get_quantity_results_of_search()
    assert  quantity_results_of_search != 0

# def test_authorization_with_phone_number(driver):
#     site = SITES(driver)
#     site.go_to_site_ge_en()
#     home_page = HomePage(driver)
#     name_button_before_login = home_page.get_name_personal_area()
#     home_page.open_pop_up_privat_area()
#     home_page.delete_symbols()
#     home_page.enter_login_tel()
#     home_page.click_proceed_button()
#     home_page.enter_password_tel()
#     home_page.click_proceed_button()
#     name_button_after_login = home_page.get_name_personal_area()
#     assert name_button_before_login != name_button_after_login
#
# def test_authorization_with_e_mail(driver):#TODO
#     site = SITES(driver)
#     site.go_to_site_ge_en()
#     home_page = HomePage(driver)
#     name_button_before_login = home_page.get_name_personal_area()
#     home_page.open_pop_up_privat_area()
#     home_page.delete_symbols()
#     home_page.enter_login_e_mail()
#     home_page.click_proceed_button()
#     home_page.enter_password_e_mail()
#     home_page.click_proceed_button()
#     name_button_after_login = home_page.get_name_personal_area()
#     assert name_button_before_login != name_button_after_login
#
# def test_authorization_google_id(driver):
#     site = SITES(driver)
#     site.go_to_site_ge_en()
#     home_page = HomePage(driver)
#     name_button_before_login = home_page.get_name_personal_area()
#     home_page.open_pop_up_privat_area()
#     home_page.click_button_google_id()#TODO
#     home_page.enter_login_google_id()
#     home_page.click_button_proceed_in_google_id()
#     home_page.enter_password_google_id()
#     home_page.click_button_proceed_in_google_id()
#     name_button_after_login = home_page.get_name_personal_area()
#     assert name_button_before_login != name_button_after_login
#
# def test_authorization_facebook_id(driver):
#     site = SITES(driver)
#     site.go_to_site_ge_en()
#     home_page = HomePage(driver)
#     name_button_before_login = home_page.get_name_personal_area()
#     home_page.open_pop_up_privat_area()
#     home_page.click_button_facebook()
#     home_page.enter_login_and_password_facebook()
#     home_page.click_button_proceed_in_facebook()
#     name_button_after_login = home_page.get_name_personal_area()
#     assert name_button_before_login != name_button_after_login
#
#
# def test_add_product_in_stock_in_cart(driver):
#     site = SITES(driver)
#     site.go_to_site_ge_en()
#     home_page = HomePage(driver)
#     time.sleep(1)#TODO
#     home_page.move_to_category("iPhone")
#     home_page.open_subcategory("iPhone 12")
#     catalog_page =CatalogPage(driver)
#     catalog_page.add_product_in_stock_in_cart()
#     catalog_page.go_to_basket()
#     cart_page = Cart(driver)
#     all_products_in_cart = cart_page.get_all_elements_in_cart()
#     assert all_products_in_cart != None
#
# def test_add_product_in_preorder_in_cart(driver):
#     site = SITES(driver)
#     site.go_to_site_ge_en()
#     home_page = HomePage(driver)
#     time.sleep(1)#TODO
#     home_page.move_to_category("iPad")
#     home_page.open_subcategory("iPad 10,2")
#     catalog_page =CatalogPage(driver)
#     catalog_page.add_product_in_preorder_in_cart()
#     catalog_page.go_to_basket()
#     cart_page = Cart(driver)
#     all_products_in_cart = cart_page.get_all_elements_in_cart()
#     assert all_products_in_cart != None