from typing import List, Tuple
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator: Tuple, time: int =10) -> WebElement:
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}"
                                                     )
    def find_elements(self, locator: Tuple, time: int =10) -> List:
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),


                                      message=f"Can't find elements by locator {locator}")

    def waits_clickable_element(self, locator: Tuple, time: int =10) -> WebElement:
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable((locator)),

                                      message = f"Element is not clickable {locator}")

    def switch_to_frame(self, locator: Tuple):
        iframe = self.find_element(locator)
        self.driver.switch_to.frame(iframe)

    def switch_to_current_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def move_to_element(self, web_elem: WebElement):
        ActionChains(self.driver).move_to_element(web_elem).perform()

    def check_absence_element(self, locator, time=5):
        WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))

    def click_with_javascript(self, web_element: WebElement) -> None:
        self.driver.execute_script("arguments[0].click();", web_element)

    def move_to_element_with_js(self, web_element: WebElement, locator: Tuple) -> None:
        """
        Goes to the element and returns it
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", web_element)
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    def delete_with_js(self, locator: Tuple,symbols: int):
        for i in range(symbols):
            self.find_element(locator).send_keys(Keys.BACKSPACE)

