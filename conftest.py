import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
import allure
import os

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="browser can be: chrome or firefox",
    )

    parser.addoption(
        "--mode",
        action="store",
        default="normal",
        help="browser mode can be: headless or normal",
    )

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    mode = request.config.getoption("--mode")

    chromedriver_path = "/home/maxim/PycharmProjects/apr_test/chromedriver"
    geckodriver_path = "/home/maxim/PycharmProjects/apr_test/geckodriver"

    download_path = "/home/maxim/Downloads"

    f_type = (
        "application/pdf"
        "vnd.ms-excel,"
        "application/vnd.ms-excel.addin.macroenabled.12,"
        "application/vnd.ms-excel.template.macroenabled.12,"
        "application/vnd.ms-excel.template.macapplication/vnd.ms-excel.sheet.binaryroenabled.12,"
        "application/vnd.ms-excel.sheet.macroenabled.12,"
        "application/octet-stream"
    )

    if browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--" + mode)
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.helperApps.alwaysAsk.force", False)
        profile.set_preference("browser.download.useDownloadDir", True)
        profile.set_preference("browser.download.dir", download_path)
        profile.set_preference("pdfjs.disabled", True)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", f_type)
        driver = webdriver.Firefox(
            profile, executable_path=geckodriver_path, options=options
        )
        driver.maximize_window()

        yield driver
        driver.quit()

    elif browser == "chrome":
        chrome_options = ChromeOptions()
        prefs = {"download.default_directory": download_path}
        chrome_options.add_argument("--" + mode)
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-setuid-sandbox")
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(
            executable_path=chromedriver_path, options=chrome_options
        )
        driver.maximize_window()

        yield driver
        driver.quit()

    elif browser == "selenoid_firefox":
        capabilities = {
            "browserName": "firefox",
            "browserVersion": "89.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=capabilities)

        driver.maximize_window()

        yield driver
        driver.quit()

    elif browser == "selenoid_chrome":
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "90.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=capabilities)

        driver.maximize_window()

        yield driver
        driver.quit()


@pytest.fixture(scope="function")
def disable_notifications(request):
    disable_notifications = request.config.getoption("--disable_notifications")
    return disable_notifications

