import pytest
from pages.home_page import HomePage
import time

def test_scrolling_banners(driver):
    driver.get("https://i-store.by")
    home_page = HomePage(driver)
    time.sleep(10) # https://asbisc.atlassian.net/browse/APR-684
    first_banner = home_page.scrolling_banners()
    time.sleep(10)
    second_banner = home_page.scrolling_banners()
    time.sleep(10)
    third_banner = home_page.scrolling_banners()
    assert first_banner != second_banner and first_banner != third_banner and second_banner != third_banner

def test_search_for_category(driver):
    driver.get("https://i-store.by")
    home_page = HomePage(driver)
    home_page.wait_send_pulse()
    home_page.close_sendpulse()
    home_page.click_search_button()
    home_page.enter_text_in_search_input()
    quantity_results_of_search = home_page.get_quantity_results_of_search_ru()
    assert  quantity_results_of_search != 0