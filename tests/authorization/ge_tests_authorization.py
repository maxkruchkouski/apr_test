import pytest
from pages.authorization_page import Authorization
from pages.home_page import HomePage
import time

def test_authorization_with_phone_number_ge(driver):
    driver.get("https://ispace.ge/")
    home_page = HomePage(driver)
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

def test_authorization_with_phone_number_en(driver):
    driver.get("https://ispace.ge/en")
    home_page = HomePage(driver)
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

def test_authorization_with_e_mail_ge(driver,):
    driver.get("https://ispace.ge/")
    home_page = HomePage(driver)
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

def test_authorization_with_e_mail_en(driver,):
    driver.get("https://ispace.ge/en/")
    home_page = HomePage(driver)
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

def test_authorization_google_id_ge(driver):
    driver.get("https://ispace.ge/")
    home_page = HomePage(driver)
    name_button_before_login = home_page.get_name_personal_area()
    home_page.open_pop_up_privat_area()
    authorization_page = Authorization(driver)
    authorization_page.click_button_google_id()
    authorization_page.enter_login_google_id()
    authorization_page.click_button_proceed_in_google_id()
    authorization_page.enter_password_google_id()
    authorization_page.click_button_proceed_in_google_id()
    name_button_after_login = home_page.get_name_personal_area_after_log_in_social_network()
    assert name_button_before_login != name_button_after_login

def test_authorization_google_id_en(driver):
    driver.get("https://ispace.ge/en/")
    home_page = HomePage(driver)
    name_button_before_login = home_page.get_name_personal_area()
    home_page.open_pop_up_privat_area()
    authorization_page = Authorization(driver)
    authorization_page.click_button_google_id()
    authorization_page.enter_login_google_id()
    authorization_page.click_button_proceed_in_google_id()
    authorization_page.enter_password_google_id()
    authorization_page.click_button_proceed_in_google_id()
    name_button_after_login = home_page.get_name_personal_area_after_log_in_social_network()
    assert name_button_before_login != name_button_after_login

@pytest.mark.skip(reason='https://asbisc.atlassian.net/browse/APR-500')
def test_authorization_facebook_id_ge(driver):
    driver.get("https://ispace.ge/")
    # driver.save_screenshot("screenshot.png")
    home_page = HomePage(driver)
    name_button_before_login = home_page.get_name_personal_area()
    home_page.open_pop_up_privat_area()
    authorization_page = Authorization(driver)
    authorization_page.click_button_facebook()
    authorization_page.enter_login_and_password_facebook()
    authorization_page.click_button_proceed_in_facebook()
    name_button_after_login = home_page.get_name_personal_area_after_log_in_social_network()
    assert name_button_before_login != name_button_after_login

@pytest.mark.skip(reason='https://asbisc.atlassian.net/browse/APR-500')
def test_authorization_facebook_id_en(driver):
    driver.get("https://ispace.ge/en/")
    # driver.save_screenshot("screenshot.png")
    home_page = HomePage(driver)
    name_button_before_login = home_page.get_name_personal_area()
    home_page.open_pop_up_privat_area()
    authorization_page = Authorization(driver)
    authorization_page.click_button_facebook()
    authorization_page.enter_login_and_password_facebook()
    authorization_page.click_button_proceed_in_facebook()
    name_button_after_login = home_page.get_name_personal_area_after_log_in_social_network()
    assert name_button_before_login != name_button_after_login