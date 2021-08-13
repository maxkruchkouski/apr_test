from pages.home_page import HomePage
import time

def test_search_for_category_ru(driver):
    driver.get("https://almastore.az/ru/")
    home_page = HomePage(driver)
    home_page.click_search_button()
    home_page.enter_text_in_search_input()
    quantity_results_of_search_ru = home_page.get_quantity_results_of_search_ru()
    assert  quantity_results_of_search_ru != 0

def test_search_for_category_az(driver):
    driver.get("https://almastore.az/")
    home_page = HomePage(driver)
    home_page.click_search_button()
    home_page.enter_text_in_search_input()
    quantity_results_of_search_az = home_page.get_quantity_results_of_search_az()
    assert quantity_results_of_search_az != 0

def test_scrolling_banners_ru(driver):
    driver.get("https://almastore.az/")
    home_page = HomePage(driver)
    first_banner = home_page.scrolling_banners()
    second_banner = home_page.scrolling_banners()
    third_banner = home_page.scrolling_banners()
    assert first_banner != second_banner and first_banner != third_banner and second_banner != third_banner

def test_scrolling_banners_az(driver):
    driver.get("https://almastore.az/")
    home_page = HomePage(driver)
    first_banner = home_page.scrolling_banners()
    second_banner = home_page.scrolling_banners()
    third_banner = home_page.scrolling_banners()
    assert first_banner != second_banner and first_banner != third_banner and second_banner != third_banner