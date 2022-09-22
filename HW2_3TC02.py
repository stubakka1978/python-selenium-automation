from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\Users\alder\python-selenium-automation\chromedriver.exe')

driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'nav-orders').click()

expected_result = 'Email or mobile phone number'
actual_result = driver.find_element(By.XPATH, "//*[@class='a-form-label']").text
assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'

print('Test case passed')
driver.quit()
