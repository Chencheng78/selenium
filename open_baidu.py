from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# open website 'baidu'.
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

config_menu = driver.find_element_by_xpath(".//*[@id='u1']/a[6]")
config_menu.click()
#ActionChains(driver).move_to_element(config_menu).perform()
sleep(5)
'''
# find the input box and send the keyword.
driver.find_element_by_name("wd").send_keys("selenium3")
# click search.
driver.find_element_by_id("su").click()
# reset the window size.
driver.set_window_size(480, 800)
sleep(1)
# try back, forward and refresh page.
driver.back()
sleep(1)
driver.forward()
sleep(1)
driver.refresh()
sleep(3)
'''
driver.quit()
