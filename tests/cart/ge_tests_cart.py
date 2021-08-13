from pages.cart_page import Cart
from pages.home_page import HomePage
from pages.catalog_page import CatalogPage
import time

def test_order_in_one_click_ge(driver):
    driver.get("https://ispace.ge/")
    home_page = HomePage(driver)
    home_page.move_to_category("Mac")
    home_page.open_subcategory('MacBook Pro')
    catalog_page = CatalogPage(driver)
    catalog_page.open_product_in_catalog()
    catalog_page.click_button_order_in_one_click()
    catalog_page.enter_name_for_order_in_one_click()
    catalog_page.enter_phone_number_for_order_in_one_click()
    catalog_page.click_button_waiting_for_a_call_for_order_in_one_click()
    toast_text = catalog_page.get_text_from_toast_after_order_in_one_click()
    assert "მადლობა! თქვენი განაცხადი მიღებულია!" in toast_text

def test_order_in_one_click_en(driver):
    driver.get("https://ispace.ge/en/")
    home_page = HomePage(driver)
    home_page.move_to_category("Mac")
    home_page.open_subcategory('MacBook Pro')
    catalog_page = CatalogPage(driver)
    catalog_page.open_product_in_catalog()
    catalog_page.click_button_order_in_one_click()
    catalog_page.enter_name_for_order_in_one_click()
    catalog_page.enter_phone_number_for_order_in_one_click()
    catalog_page.click_button_waiting_for_a_call_for_order_in_one_click()
    toast_text = catalog_page.get_text_from_toast_after_order_in_one_click()
    assert "Thanks! Your application has been sent!" in toast_text

def test_add_product_in_stock_to_cart_ge(driver):
    driver.get("https://ispace.ge/")
    home_page = HomePage(driver)
    home_page.move_to_category("Mac")
    home_page.open_subcategory('MacBook Pro')
    catalog_page =CatalogPage(driver)
    catalog_page.add_product_in_stock_in_cart()
    product_name_and_sku = catalog_page.get_product_name_and_sku_in_pop_up_for_ge()
    product_cost = catalog_page.get_product_cost_in_pop_up_for_ge()
    catalog_page.go_to_basket_for_ge()
    cart_page = Cart(driver)
    all_products_in_cart = cart_page.get_all_elements_in_cart()
    cart_total_cost = cart_page.get_total_cost_in_cart()
    assert product_name_and_sku  in all_products_in_cart
    assert product_cost == cart_total_cost
#
# def test_add_product_in_stock_to_cart_en(driver):
#     driver.get("https://ispace.ge/en/")
#     home_page = HomePage(driver)
#     home_page.move_to_category("Mac")
#     home_page.open_subcategory('iMac 24')
#     catalog_page =CatalogPage(driver)
#     catalog_page.add_product_in_stock_in_cart()
#     product_name_and_sku = catalog_page.get_product_name_and_sku_in_pop_up_for_ge()
#     product_cost = catalog_page.get_product_cost_in_pop_up_for_ge()
#     catalog_page.go_to_basket_for_ge()
#     cart_page = Cart(driver)
#     all_products_in_cart = cart_page.get_all_elements_in_cart()
#     cart_total_cost = cart_page.get_total_cost_in_cart()
#     assert product_name_and_sku  in all_products_in_cart
#     assert product_cost == cart_total_cost
#
# def test_add_product_in_preorder_to_cart_ge(driver):
#     driver.get("https://ispace.ge/")
#     home_page = HomePage(driver)
#     home_page.move_to_category("iPhone")
#     home_page.open_subcategory('iPhone 12')
#     catalog_page = CatalogPage(driver)
#     catalog_page.add_product_in_preorder_in_cart()
#     product_name_and_sku = catalog_page.get_product_name_and_sku_in_pop_up_for_ge()
#     product_cost = catalog_page.get_product_cost_in_pop_up_for_ge()
#     catalog_page.go_to_basket_for_ge()
#     cart_page = Cart(driver)
#     all_products_in_cart = cart_page.get_all_elements_in_cart()
#     cart_total_cost = cart_page.get_total_cost_in_cart()
#     assert product_name_and_sku in all_products_in_cart
#     assert product_cost == cart_total_cost
#
# def test_add_product_in_preorder_to_cart_en(driver):
#     driver.get("https://ispace.ge/en/")
#     home_page = HomePage(driver)
#     home_page.move_to_category("iPad")
#     home_page.open_subcategory('iPad Air 4')
#     catalog_page = CatalogPage(driver)
#     catalog_page.add_product_in_preorder_in_cart()
#     product_name_and_sku = catalog_page.get_product_name_and_sku_in_pop_up_for_ge()
#     product_cost = catalog_page.get_product_cost_in_pop_up_for_ge()
#     catalog_page.go_to_basket_for_ge()
#     cart_page = Cart(driver)
#     all_products_in_cart = cart_page.get_all_elements_in_cart()
#     cart_total_cost = cart_page.get_total_cost_in_cart()
#     assert product_name_and_sku in all_products_in_cart
#     assert product_cost == cart_total_cost