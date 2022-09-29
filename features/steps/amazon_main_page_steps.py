from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')



@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(product)
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()
