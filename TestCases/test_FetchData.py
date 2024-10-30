from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
#from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest


@pytest.fixture()
def environmet_setup():
    global driver
    driver = Firefox()
    #driver.set_page_load_timeout(1)
    driver.get("https://thetestingworld.com/testings")  # Step2

    # Maximize browser
    driver.implicitly_wait(5)
    driver.maximize_window()  # Step3
    yield
    driver.close()

def test_verify_registration(environmet_setup):
    # wait = WebDriverWait(driver, 100)
    # wait.until(ec.text_to_be_present_in_element(By.NAME, "India"))

    # # Enter Data to the text box
    obj = Select(driver.find_element(By.ID, "countryId"))
    obj.select_by_visible_text("India")

    obj = Select(driver.find_element(By.ID, "stateId"))
    obj.select_by_visible_text("Delhi")
    # driver.find_element(By.NAME, "fld_username").send_keys("HelloWorld") #Step4
    # driver.find_element(By.XPATH, "//*[@id='tab-content1']/form/input[3]").send_keys("test@helloworld.com")
    # driver.find_element(By.XPATH, "//*[@id='tab-content1']/form/input[3]").clear()
    # driver.find_element(By.XPATH, "//*[@id='tab-content1']/form/input[3]").send_keys("testing123@helloworld.com")
    # driver.find_element(By.NAME, "fld_password").send_keys("abcd123")
    # driver.find_element(By.NAME, "fld_cpassword").send_keys("abcd123")
    #
    # # Work on Dropdown
    # obj = Select(driver.find_element(By.NAME, "sex11"))  # Step10
    # # obj.select_by_value("1")
    # # obj.select_by_index(2)
    # obj.select_by_visible_text("Male")
    #
    # # obj.deselect_by_index(2) # Only for List values
    #
    # # Working on Radio Button
    # driver.find_element(By.XPATH, "//input[@value = 'home']").click()  # Step 5
    # driver.find_element(By.XPATH, "//input[@value = 'office']").click()
    #
    # # Working on Checkbox
    # driver.find_element(By.NAME, "terms").click()  # Step6
    #
    # # Working on Button
    # driver.find_element(By.XPATH, "//input[@value = 'Sign up']").click()#Step7
    #
    # # Working on Link
    # #driver.find_element(By.XPATH, "//a[@value = ''").click()
    # driver.find_element(By.LINK_TEXT, "Read Detail").click()#Step8
    #
    # assert driver.current_url == "https://thetestingworld.com/testings/"


#path = "C:\\chromedriver.exe" #Chrome
#path = "C:\\geckodriver.exe" #Firefox

#driver = Chrome() #Chrome
#driver = Firefox()
#driver.get("https://thetestingworld.com/testings") #Step2

# #Maximize browser
# driver.maximize_window() #Step3
#
# #Fetching title
# print("Title of page is: " + driver.title)
#
# #Fetch URL of page
# print("Page URL is: " + driver.current_url)
#
# #Fetch complete Page HTML
# print("****************************************************************************")
# print(driver.page_source)

#Fetching Element Text
# print("Texto on Link is: " + driver.find_element(By.CLASS_NAME, "displayPopup").text)
#
# #Fetching attribute value of Element
# print("Value of button is: " + driver.find_element(By.XPATH, "//input[@type='submit']").get_attribute("value"))

#Fetching Data from Dropdown List
#bj = Select(driver.find_element(By.NAME, "sex"))#Step10
#obj.select_by_visible_text("Male")

#Fetch Selected option
#print(obj.first_selected_option.text)

#print("****************************************************************")
#Fetch all options
#for op in obj.options:
#    print(op.text)
