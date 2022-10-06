from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(product)
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}')


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()
    sleep(2)


@when('Store product name')
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME)