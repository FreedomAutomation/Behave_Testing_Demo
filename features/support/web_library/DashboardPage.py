from features.support.web_library.BasePage import BasePage
from selenium.webdriver.common.by import By
from features.support.web_library.LoginPage import LOGIN_BUTTON, BURGER_MENU

LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")

class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def logout(self):
        self.click(BURGER_MENU)
        self.click(LOGOUT_BUTTON)

    def is_redirected_to_login(self):
        # Check if redirected to the login page based on some element on the login page
        try:
            self.wait_for_element_visibility(LOGIN_BUTTON)
            return True
        except:
            return False