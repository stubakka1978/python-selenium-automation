from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click Returns & Orders')
def click_signin_button(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@when('Click Cart')
def click_cart_button(context):
    context.driver.find_element(By.ID, 'nav-cart').click()