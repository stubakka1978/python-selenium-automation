from selenium.webdriver.common.by import By
from behave import given, when, then

BestSellers_LINKS = (By.CSS_SELECTOR, '._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq li')

@then('Verify that page has {expected_link_count1} links')
def verify_page_link_count(context, expected_link_count1):
    expected_link_count1 = int(expected_link_count1)

    links1 = context.driver.find_elements(*BestSellers_LINKS)

    assert len(links1) == expected_link_count1, \
        f'Expected {expected_link_count1} links, but got {len(links1)}'