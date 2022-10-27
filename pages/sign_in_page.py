from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    SIGNIN = (By.ID, 'nav-orders')

    def open_sign_in(self):
        self.open_url('ap/signin')

    def click_signin_button(self):
        self.driver.find_element(*self.SIGNIN).click()