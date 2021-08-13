import pytest
from pages.cart_page import Cart
from pages.home_page import HomePage
from pages.catalog_page import CatalogPage
from pages.checkout_page import CheckoutPage
import time

def test_order_in_one_click(driver):
    driver.get("https://i-store.by")
    home_page = HomePage(driver)
    home_page.wait_send_pulse()
    home_page.close_sendpulse()
    home_page.move_to_category("Mac")
    home_page.open_subcategory('MacBook Pro')
    catalog_page = CatalogPage(driver)
    catalog_page.open_product_in_catalog()
    catalog_page.click_button_order_in_one_click()
    catalog_page.enter_name_for_order_in_one_click()
    catalog_page.enter_phone_number_for_order_in_one_click()
    catalog_page.click_button_waiting_for_a_call_for_order_in_one_click()
    toast_text = catalog_page.get_text_from_toast_after_order_in_one_click()
    assert "Спасибо! Ваша заявка отправлена!" in toast_text


def test_add_product_in_stock_to_cart(driver):
    driver.get("https://i-store.by")
    home_page = HomePage(driver)
    home_page.wait_send_pulse()
    home_page.close_sendpulse()
    home_page.move_to_category("Mac")
    home_page.open_subcategory('MacBook Pro')
    catalog_page =CatalogPage(driver)
    catalog_page.add_product_in_stock_in_cart()

    product_name_and_sku = catalog_page.get_product_name_and_sku_in_pop_up()
    product_cost = catalog_page.get_product_cost_in_pop_up()
    catalog_page.go_to_basket()
    cart_page = Cart(driver)
    all_products_in_cart = cart_page.get_all_elements_in_cart()
    cart_total_cost = cart_page.get_total_cost_in_cart()
    assert product_name_and_sku  in all_products_in_cart
    assert product_cost == cart_total_cost
    # cart_page.open_input_promo_code()
    # cart_page.enter_promo_code()
    # cart_page.click_proceed_promo_code()
    # cart_page.click_button_submit_order()
    # checkout_page = CheckoutPage(driver)
    # checkout_page.enter_name_on_checkout_page()
    # checkout_page.enter_phone_number_on_checkout_page()
    # checkout_page.enter_email_on_checkout_page()
    # checkout_page.send_comment()
    # checkout_page.click_button_delivery_across_belarus()




def test_add_product_in_preorder_to_cart(driver):
    driver.get("https://i-store.by")
    home_page = HomePage(driver)
    home_page.wait_send_pulse()
    home_page.close_sendpulse()
    home_page.move_to_category("iPhone")
    home_page.open_subcategory('iPhone 12 Pro Max')
    catalog_page = CatalogPage(driver)
    catalog_page.add_product_in_preorder_in_cart()
    product_name_and_sku = catalog_page.get_product_name_and_sku_in_pop_up()
    product_cost = catalog_page.get_product_cost_in_pop_up()
    catalog_page.go_to_basket()
    cart_page = Cart(driver)
    all_products_in_cart = cart_page.get_all_elements_in_cart()
    cart_total_cost = cart_page.get_total_cost_in_cart()
    assert product_name_and_sku in all_products_in_cart
    assert product_cost == cart_total_cost

