from selenium.webdriver import Firefox
#from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#path = "C:\\chromedriver.exe" #Chrome
#path = "C:\\geckodriver.exe" #Firefox

#driver = Chrome() #Chrome
driver = Firefox()
driver.get("https://thetestingworld.com/testings") #Step2

#Maximize browser
driver.maximize_window() #Step3

#Enter Data to the text box
# driver.find_element(By.NAME, "fld_username").send_keys("HelloWorld") #Step4
# driver.find_element(By.XPATH, "//*[@id='tab-content1']/form/input[3]").send_keys("test@helloworld.com")
# driver.find_element(By.XPATH, "//*[@id='tab-content1']/form/input[3]").clear()
# driver.find_element(By.XPATH, "//*[@id='tab-content1']/form/input[3]").send_keys("testing123@helloworld.com")
# driver.find_element(By.NAME, "fld_password").send_keys("abcd123")
# driver.find_element(By.NAME, "fld_cpassword").send_keys("abcd123")

#Work on Dropdown
obj = Select(driver.find_element(By.NAME, "sex"))#Step10
#obj.select_by_value("1")
#obj.select_by_index(2)
#obj.select_by_visible_text("Male")

#obj.deselect_by_index(2) # Only for List values

#Working on Radio Button
driver.find_element(By.XPATH, "//input[@value = 'home']").click()#Step 5
driver.find_element(By.XPATH, "//input[@value = 'office']").click()

#Working on Checkbox
driver.find_element(By.NAME, "terms").click() #Step6

#Working on Button
#driver.find_element(By.XPATH, "//input[@value = 'Sign up']").click()#Step7

#Working on Link
#driver.find_element(By.XPATH, "//a[@value = ''").click()
#driver.find_element(By.LINK_TEXT, "Read Detail").click()#Step8

#Close my browser
#driver.close()#Step 9