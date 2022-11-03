from selenium.webdriver.common.by import By
from behave import given, when, then

HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem a')


@given('Open amazon page')
def open_amazon(context):
    context.app.main_page.open_main()


@when('Click Best Sellers')
def click_bestsellers_page(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/bestsellers/?ref_=nav_cs_bestsellers']").click()


@when('Hover over language options')
def hover_lang(context):
    context.app.main_page.hover_lang()


@when('Select department by value {selection_value}')
def select_department(context, selection_value):
    context.app.main_page.select_department(selection_value)


@when('Hover over New Arrivals')
def hover_new_arrivals(context):
    context.app.main_page.hover_new_arrivals()


@then('Verify {department} department is selected')
def verify_department(context, department):
    context.app.search_results_page.verify_department(department)


@then('Verify hamburger menu is present')
def verify_ham_menu_present(context):
    context.driver.find_element(*HAM_MENU)


@then('Verify that footer has {expected_link_count} links')
def verify_link_count(context, expected_link_count):
    expected_link_count = int(expected_link_count)

    links = context.driver.find_elements(*FOOTER_LINKS)

    assert len(links) == expected_link_count, \
        f'Expected {expected_link_count} links, but got {len(links)}'


@then('Verify Spanish option present')
def verify_lang(context):
    context.app.main_page.verify_lang()


@then('Verify New Arrival deals')
def verify_new_arrivals(context):
    context.app.main_page.verify_new_arrivals()
