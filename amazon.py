import pytest
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



class TestAmazonCreateAccount():
  
 driver = webdriver.Chrome()
 
  
 

  
 def read_rows(filename):
    items = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            items.append(row)
   
    return items

 testdata=read_rows('amazon.csv')




 def setup_method(self):
    self.driver.get("https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_ya_signin&prevRID=PFTBT98E73CM644MKBXG&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    self.driver.maximize_window()
    
    
 
  
 

  
 @pytest.mark.parametrize('name,email,password,re_enter,expected',testdata)
 def test_amazon(self,name,email,password,re_enter,expected):
    name_field=self.driver.find_element_by_xpath('//*[@id="ap_customer_name"]')
    email_field=self.driver.find_element(By.ID, "ap_email")
    password_field=self.driver.find_element(By.XPATH, '//*[@id="ap_password"]')
    confirm_password_field=self.driver.find_element(By.ID, 'ap_password_check')
    button=self.driver.find_element(By.ID, 'continue')

    name_field.clear()
    name_field.send_keys(name)
   
    email_field.clear()
    email_field.send_keys(email)
   
    password_field.clear()
    password_field.send_keys(password)

    confirm_password_field.clear()
    confirm_password_field.send_keys(re_enter)
    
    button.click()
 
    assert expected in self.driver.title   

 
 
