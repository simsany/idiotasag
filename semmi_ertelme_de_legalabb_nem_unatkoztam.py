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



class TestJojo():
  def read_rows(filename):
    items = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            items.append(row)
   
    return items


  driver = webdriver.Chrome()
  testdata=read_rows('selenium_two_fields.csv')
  def setup_method(self, method):

    
    self.driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
  
    try:
      self.driver.find_element(By.XPATH,'//*[@id="at-cv-lightbox-close"]').click()
    except:
      pass
    self.driver.maximize_window()
    
 
  def teardown_method(self, method):
    pass
 

  
  @pytest.mark.parametrize('a,a_exp,b,b_exp,expected',testdata)
 
  
  def test_jojo(self,a,a_exp,b,b_exp,expected):
    
    
    field1=self.driver.find_element(By.ID, "sum1")
    field2=self.driver.find_element(By.ID, "sum2")
    button=self.driver.find_element(By.XPATH, '//*[@id="gettotal"]/button')
    result=self.driver.find_element(By.ID, 'displayvalue')

  
    field1.clear()
    time.sleep(1)
    field1.send_keys(a)
    assert field1.get_attribute('value') == a_exp
    field2.clear()
    time.sleep(1)
    field2.send_keys(b)
    assert field2.get_attribute('value') == b_exp
    
    button.click()
    time.sleep(1)
    assert result.get_attribute('innerHTML') == expected
 
 
