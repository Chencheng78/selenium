from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://mail.163.com")
# switch to the login frame
driver.switch_to.frame("x-URS-iframe")
# clear the box first and input username and password.
driver.find_element_by_name('email').clear()
driver.find_element_by_name('email').send_keys('geniuscc7')
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('tensaiccalex1988')
# click login button.
driver.find_element_by_css_selector('#dologin').click()

driver.quit()
