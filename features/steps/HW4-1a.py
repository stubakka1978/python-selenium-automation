from selenium.webdriver.common.by import By
from behave import given, when, then


HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem a')



@given('Open amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@then('Verify hamburger menu is present')
def verify_ham_menu_present(context):
    context.driver.find_element(*HAM_MENU)


@then('Verify that footer has {expected_link_count} links')
def verify_link_count(context, expected_link_count):
    expected_link_count = int(expected_link_count)

    links = context.driver.find_elements(*FOOTER_LINKS)

    assert len(links) == expected_link_count, \
        f'Expected {expected_link_count} links, but got {len(links)}'


@when('Click Best Sellers')
def click_bestsellers_page(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/bestsellers/?ref_=nav_cs_bestsellers']").click()
