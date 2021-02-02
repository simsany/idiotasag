import time
import bcolors
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# Steps to Automate:
# 1. Launch browser of your choice say., Firefox, chrome etc.
# 2. Open this URL - https://www.godaddy.com/
# 3. Maximize or set size of browser window.
# 4. Get Title of page and validate it with expected value.
# 5. Get URL of current page and validate it with expected value.
# 6. Get Page source of web page.
# 7. And Validate that page title is present in page source.
# 8. Close browser.


driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
links=driver.find_elements_by_css_selector('a[data-csa-c-slot-id^="nav_cs"]' )
for i in range(7):
    try:
        links=driver.find_elements_by_css_selector('a[data-csa-c-slot-id^="nav_cs"]' )
        time.sleep(1)
        innerHTML=links[i].get_attribute("innerHTML")
        links[i].click()
        
        time.sleep(1)
        if  innerHTML in driver.title:
            
            
            print(f'{bcolors.OK}{innerHTML} is in {driver.title}  PASS')
        else:
            print(f'{bcolors.FAIL}{innerHTML} is not in {driver.title}  FAIL')
        driver.back()
        time.sleep(2)
        

    except:
        driver.close()


   
