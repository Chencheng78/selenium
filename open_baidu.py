from selenium import webdriver


driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_name("wd").send_keys("selenium3")
driver.find_element_by_id("su").click()
#driver.quit()
