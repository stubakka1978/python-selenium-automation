from behave import then
from selenium.webdriver.support import expected_conditions as EC


@then('Verify blog is opened')
def verify_blog_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.aboutamazon.com/news/workplace/'))


@then('Close blog')
def close_blog(context):
    context.driver.close()


@then('Return to original window')
def return_to_original(context):
    context.driver.switch_to.window(context.original_window)
