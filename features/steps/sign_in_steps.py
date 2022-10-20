from time import sleep
from selenium.webdriver.common.by import By
from behave import when, then
from selenium.webdriver.support import expected_conditions as EC

SIGN_IN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-button')


@when('Wait for {sec} sec')
def wait_sec(context, sec):
    sleep(int(sec))


@then('Verify Sign In is clickable')
def verify_sign_in_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN), message='Sign in not clickable')


@then('Verify Sign In disappears')
def verify_sign_in_btn_disappears(context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGN_IN), message='Sign in is still visible')
