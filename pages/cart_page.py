from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART = (By.ID, 'nav-cart')

    def open_cart(self):
        self.open_url('ap/signinview.html?ref_=nav_cart')

    def click_cart_button(self):
        self.driver.find_element(*self.CART).click()