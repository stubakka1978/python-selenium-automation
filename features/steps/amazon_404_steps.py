from selenium.webdriver.common.by import By
from behave import given, when
from selenium.webdriver.support import expected_conditions as EC

DOG_IMG = (By.CSS_SELECTOR, "img[alt='Dogs of Amazon']")


@given('Store original window')
def store_window(context):
    context.original_window = context.driver.current_window_handle


@when('Click on a dog image')
def click_img(context):
    context.driver.find_element(*DOG_IMG).click()


@when('Switch to new window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    context.driver.switch_to.window(current_windows[1])

