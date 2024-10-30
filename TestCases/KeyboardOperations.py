from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = Firefox()
driver.get("https://thetestingworld.com/testings")
driver.find_element(By.NAME, "fld_username").send_keys("Hello")

action = ActionChains(driver)
keys = Keys()
#Control + a
#action.key_down(keys.CONTROL).send_keys('a').perform()
time.sleep(5)
driver.find_element(By.NAME, "fld_username").send_keys("This is a test")
time.sleep(5)
action.key_down(keys.CONTROL).send_keys('a').perform()
#action.key_down(keys.CONTROL).key_down(keys.ALT).send_keys(keys.DELETE).perform()
#action.send_keys(keys.TAB)
