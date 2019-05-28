from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600') # optional

#Set to HEADLESS Chrome Driver (UNCOMMENT BELOW LINE)
#driver = webdriver.Chrome(chrome_options=options) #un-comment for headless
#driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver 4')

#Set to Chrome Driver (UNCOMMENT BELOW LINE TO SEE BROWSER SIMULATED ACTIONS)
print('\n---NOW STARTING CHROME SERVER---\n')
#driver = webdriver.Chrome() #--Only use this line if you are working in windows
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver 4') #must start driver with chromedriver 4

#Go to Tours page
driver.get("https://www.architecture.org/tours")
print('\nRetrieving Tours Page\n')

#Scroll search area into view
CHI_BTN_Tour = driver.find_element_by_class_name('tour_search')
#Use JavaScript Executor to click on element
driver.execute_script("arguments[0].scrollIntoView();", CHI_BTN_Tour)
print('Scrolling down to Search Area\n')

#use action to scroll element into view
action = ActionChains(driver);
walkTour = driver.find_element_by_xpath('//*[@id="search"]/section/div/div[1]/div[3]/div[1]/div/button[2]')
action.move_to_element(walkTour).perform();
time.sleep(2)
walkTour.send_keys(Keys.RETURN)

print('Navigating To "Walking Tours" hyperlink\n')

walkTime_BTN_Tour = driver.find_element_by_xpath('//*[@id="events_view"]/div[2]/div[1]/article[3]/div/div[2]/div/p/a[1]')
#Use JavaScript Executor to click on element
driver.execute_script("arguments[0].scrollIntoView();", walkTime_BTN_Tour)
print('Scrolling down to "A WALK THROUGH TIME" tour\n')
time.sleep(2)

#use action to scroll element into view
action = ActionChains(driver);
walkLearnMore_BTN = driver.find_element_by_xpath('//*[@id="events_view"]/div[2]/div[1]/article[2]/div/div[2]/div/p/a[1]')
action.move_to_element(walkLearnMore_BTN).perform();
time.sleep(2)
walkLearnMore_BTN.send_keys(Keys.RETURN)

print('Learn More Button Has Been Pressed\n')

print('Saving a screenshot of final browser window\n')
#driver.save_screenshot(r'''C:\Users\Owner\Documents\MyPyTests\IndustrySignUpNews.png''')

driver.save_screenshot(r'''Screenshots\walkthroughtime.png''')


print('Closing the driver to exit the browser window in 10 seconds\n')

time.sleep(10)

driver.close()

print('**********TEST RUN SUCCESSFULLY COMPLETED**********')

