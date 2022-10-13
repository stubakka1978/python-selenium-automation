from selenium.webdriver.common.by import By
from behave import when
from selenium.webdriver.support import expected_conditions as EC


PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")


@when('Click on the first product')
def click_first_product(context):
    # sleep(2)
    e = context.driver.wait.until(EC.element_to_be_clickable(PRODUCT_PRICE), message='PRODUCT_PRICE not clickable')
    e.click()
