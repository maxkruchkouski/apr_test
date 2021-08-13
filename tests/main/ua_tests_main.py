from pages.home_page import HomePage
import time

def test_search_for_category_ru(driver):
    driver.get("https://ion.ua/")
    home_page = HomePage(driver)
    home_page.click_search_button()
    home_page.enter_text_in_search_input()
    quantity_results_of_search = home_page.get_quantity_results_of_search_ru()
    assert  quantity_results_of_search != 0

def test_search_for_category_ua(driver):
    driver.get("https://ion.ua/ua/")
    home_page = HomePage(driver)
    home_page.click_search_button()
    home_page.enter_text_in_search_input()
    quantity_results_of_search = home_page.get_quantity_results_of_search_ua()
    assert  quantity_results_of_search != 0

def test_scrolling_banners_ru(driver):
    driver.get("https://ion.ua/")
    home_page = HomePage(driver)
    first_banner = home_page.scrolling_banners()
    second_banner = home_page.scrolling_banners()
    third_banner = home_page.scrolling_banners()
    assert first_banner != second_banner and first_banner != third_banner and second_banner != third_banner


def test_scrolling_banners_ua(driver):
    driver.get("https://ion.ua/ua")
    home_page = HomePage(driver)
    first_banner = home_page.scrolling_banners()
    second_banner = home_page.scrolling_banners()
    third_banner = home_page.scrolling_banners()
    assert first_banner != second_banner and first_banner != third_banner and second_banner != third_banner
