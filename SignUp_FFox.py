#!/usr/bin/python
# -*- coding: utf8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
import datetime
import time


#options = Options()
#options.add_argument("--headless")
#driver = Firefox(firefox_options=options)

driver= webdriver.Firefox()
#driver= webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.implicitly_wait(10)

#set date/time to create new user and email
Today = int(datetime.datetime.now().timestamp())

#Go to Industry News sign-up form
driver.get("http://www.architecture.org/get-involved/industry-email-sign-up/")

# Fill Out & Submit The Form
#FirstName = driver.find_element_by_id(form_builder_field_1)

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

driver.execute_script('window.scrollTo(0,500)')
time.sleep(2)
PostalCode = driver.find_element_by_id('form_builder_field_5')
PostalCode.send_keys('60611')
#print('Postal Code: ' + str(PostalCode))
print('Postal Code: ' + str(PostalCode.get_attribute('value')))
#driver.execute_script('scroll(0, 250);') #-scroll works

action = ActionChains(driver);
Country = driver.find_element_by_xpath('//*[@id="form_builder_field_7-dropdown-selected"]')
Country.click()
time.sleep(2)
Canada = driver.find_element_by_xpath('//*[@id="form_builder_field_7-dropdown"]/div/button[3]')
action.move_to_element(Canada).perform();
Canada.click()
time.sleep(2)
print('Country Selected: '+ str(Canada.get_attribute('innerHTML')))

Company = driver.find_element_by_id('form_builder_field_8')
Company.send_keys("Chicago Architecture Center")
#print('Company: ' + str(Company))

print('Company: ' + str(Company.get_attribute('value')))
time.sleep(2)

checkboxEventPlanners = driver.find_element_by_id("form_builder_field_9")
driver.execute_script("arguments[0].click();", checkboxEventPlanners)
time.sleep(2)

wait = WebDriverWait(driver, 10)

EventPlanner_result = wait.until(ec.element_located_selection_state_to_be((By.ID, 'form_builder_field_9'), True))
print('Event Planners Checkbox has been selected: ' + str(EventPlanner_result))

print('Checkbox selection is: ' + str(checkboxEventPlanners.get_attribute('value')))

checkboxConcierges = driver.find_element_by_id('form_builder_field_10')
driver.execute_script("arguments[0].click();", checkboxConcierges)
time.sleep(2)

Concierges_result = wait.until(ec.element_located_selection_state_to_be((By.ID, 'form_builder_field_10'), True))
print('Concierges Checkbox has been selected: ' + str(Concierges_result))

print('Checkbox selection is: ' + str(checkboxConcierges.get_attribute('value')))

#SubmitBtn = driver.find_element_by_value('Submit')
#SubmitBtn.send_keys(Keys.RETURN)

#takes a screenshot of the webpage
#driver.save_screenshot(r'''C:\Users\Owner\Documents\MyPyTests\FFox_IndSignUp.png''') #for windows screenshot
#driver.save_screenshot('FFox_IndSignUp.png') #FIX - this won't work for MAC screenshot

print('TEST RUN COMPLETED')
time.sleep(10)
driver.close()

