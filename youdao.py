from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.youdao.com")

driver.find_element_by_css_selector('#translateContent').send_keys('hello')
# use submit method after the keyword is input in the box to simulate 'enter'  button.
driver.find_element_by_css_selector('#translateContent').submit()
# driver.find_element_by_css_selector('#form>button').click()

sleep(5)
driver.quit()
