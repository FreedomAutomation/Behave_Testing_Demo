from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def wait_for_element_visibility(self, element):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element))

    def wait_for_element_invisibility(self,element):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(element))\

    def click_back_button(self):
        self.driver.back()
