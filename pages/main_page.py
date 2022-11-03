from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page
from selenium.webdriver.support.ui import Select


class MainPage(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    LANG_SELECTION = (By.CSS_SELECTOR, '.icp-nav-flag-us')
    SPANISH_LANG = (By.CSS_SELECTOR, '#nav-flyout-icp [href="#switch-lang=es_US"]')
    DEPARTMENT_SELECTION = (By.ID, 'searchDropdownBox')
    NEW_ARRIVALS = (By.CSS_SELECTOR, "a[href*='/New-Arrivals/b/?']")
    SEE_DEALS = (By.CSS_SELECTOR, '.mm-category-list')

    def open_main(self):
        self.open_url()

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

    def hover_lang(self):
        language_selection = self.find_element(*self.LANG_SELECTION)
        actions = ActionChains(self.driver)
        actions.move_to_element(language_selection)
        actions.perform()

    def hover_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def select_department(self, selection_value):
        select = Select(self.find_element(*self.DEPARTMENT_SELECTION))
        select.select_by_value(f'search-alias={selection_value}')

    def verify_lang(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def verify_new_arrivals(self):
        self.wait_for_element_appear(*self.SEE_DEALS)

