from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = Firefox()
driver.get("https://thetestingworld.com/")

#Mouseclick Operations
action = ActionChains(driver)
#action.context_click().perform()
#driver.find_element(By.XPATH, "//a[text()='Quick Demo']").click()

#Left click
# action.click(driver.find_element(By.XPATH, "//a[text()='Quick Demo']")).perform()
# time.sleep(5)

# Right click
# action.context_click(driver.find_element(By.NAME, "wdform_1_element_first2")).perform()
time.sleep(5)
action.move_to_element(driver.find_element(By.XPATH, "//span[text()='TUTORIAL ']")).perform()
#action.move_to_element(driver.find_element(By.XPATH, "//*[@id='menu516']/span")).perform()
time.sleep(5)


