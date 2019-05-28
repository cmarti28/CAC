from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
#from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600') # optional

#Set to HEADLESS Chrome Driver (UNCOMMENT BELOW LINE)
#driver = webdriver.Chrome(chrome_options=options) #un-comment for headless
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver 4')


#Set to Chrome Driver (UNCOMMENT BELOW LINE TO SEE BROWSER SIMULATED ACTIONS)
#driver = webdriver.Chrome()

#Go to Industry News sign-up form
#driver.get("http://www.architecture.org/get-involved/industry-email-sign-up/")
driver.get("http://rest.caftest.org//get-involved/industry-email-sign-up/")

# Fill Out & Submit The Form

#set date/time to milliseconds to create unique new user and email names
Today = int(datetime.datetime.now().timestamp())

FirstName=driver.find_element_by_xpath('//*[@id="form_builder_field_1"]')

FirstName.send_keys('Joyful-' + str(Today)) 
#print('First Name: ' + str(FirstName) + str(FirstName.get_attribute('value')))

print('First Name: ' + str(FirstName.get_attribute('value')))

LastName = driver.find_element_by_id('form_builder_field_2')
LastName.send_keys('Happy-' + str(Today))
#print('Last Name: ' + str(LastName))

print('Last Name: ' + str(LastName.get_attribute('value')))

EmailAddress = driver.find_element_by_id('form_builder_field_3')
EmailAddress.send_keys('joyfulemail'+ str(Today) + '@happy.com')
#print('Email Address: ' + str(EmailAddress.get_attribute('value')))
print('Email Address: ' + str(EmailAddress.get_attribute('value')))

PostalCode = driver.find_element_by_id('form_builder_field_5')
PostalCode.send_keys('60601')
#print('Postal Code: ' + str(PostalCode))
print('Postal Code: ' + str(PostalCode.get_attribute('value')))

action = ActionChains(driver);
#Country = driver.find_element_by_id('form_builder_field_7-dropdown-selected')
#For country, the following line works on a mac for chrome but now windows
Country = driver.find_element_by_xpath('//*[@id="form_builder_field_7-dropdown-selected"]')
#the following line works on windows
#Country = driver.find_element_by_xpath('//*[@id="form_builder_field_7-dropdown"]/div/button[3]')
time.sleep(2)
Country.click()
Canada = driver.find_element_by_xpath('//*[@id="form_builder_field_7-dropdown"]/div/button[3]')
action.move_to_element(Canada).perform();
Canada.click()
#print('Country Selected: ' + str(Canada))
print('Country Selected: '+ str(Canada.get_attribute('innerHTML')))

Company = driver.find_element_by_id('form_builder_field_8')
Company.send_keys("Chicago Architecture Center")
#print('Company: ' + str(Company))

print('Company: ' + str(Company.get_attribute('value')))
#time.sleep(2)

checkboxEventPlanners = driver.find_element_by_id("form_builder_field_9")
driver.execute_script("arguments[0].click();", checkboxEventPlanners)
time.sleep(2)

print('Checkbox selection is: ' + str(checkboxEventPlanners.get_attribute('value')))

checkboxConcierges = driver.find_element_by_id('form_builder_field_10')
driver.execute_script("arguments[0].click();", checkboxConcierges)
time.sleep(2)

print('Checkbox selection is: ' + str(checkboxConcierges.get_attribute('value')))

SubmitBTN = driver.find_element_by_xpath('//*[@id="pagecontent"]/main/div[2]/div[2]/form/input')
SubmitBTN.send_keys(Keys.RETURN)

#takes a screenshot of the webpage
#driver.save_screenshot(r'''C:\Users\Owner\Documents\MyPyTests\IndustrySignUpNews.png''')

print('TEST RUN COMPLETED')
#time.sleep(10)
#driver.close()

