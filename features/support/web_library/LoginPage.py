from selenium.common import ElementNotVisibleException

from features.support.web_library.BasePage import BasePage
from selenium.webdriver.common.by import By

USERNAME_FIELD = (By.ID, "user-name")
PASSWORD_FIELD = (By.ID, "password")
LOGIN_BUTTON = (By.ID, "login-button")
ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container error")
BURGER_MENU = (By.ID, "react-burger-menu-btn")

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"  # Replace with your actual login page URL

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.enter_text(USERNAME_FIELD, username)
        self.enter_text(PASSWORD_FIELD, password)
        self.click(LOGIN_BUTTON)

    def error_message_displayed(self, expected_error):
        try:
            self.wait_for_element_visibility((By.XPATH, f'//*[contains(text(),"{expected_error}")]'))
            return True
        except ElementNotVisibleException:
            return False

    def error_message_is_not_displayed(self):
        try:
            self.wait_for_element_invisibility(ERROR_MESSAGE)
            return True
        except:
            return False

    def is_logged_in(self):
        # Check if a user is logged in based on some element on the dashboard
        try:
            self.wait_for_element_visibility(BURGER_MENU)
            return True
        except:
            return False
