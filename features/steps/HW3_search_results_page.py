from selenium.webdriver.common.by import By
from behave import given, when, then

@then('User is able to sign into account')
def verify_signin_results(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class ='a-spacing-small']").text
    assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
    assert context.driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field not shown'


@then('User is able to see cart is empty')
def verify_cart_results(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//h2").text
    assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'