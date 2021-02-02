import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def get_neighbours(element):
    
    element_coords=element.get_attribute('id').split('_')
    start=[int(element_coords[0])-1,int(element_coords[1])-1]
    nb_coords=[]
    for i in range(3):
        for j in range(3):
            nb_coords.append([start[0]+i,start[1]+j])
    nb_coords.pop(4)
   
    return nb_coords

def get_valid_nbs(nb_list):
    invalid_row=[-1,17]
    invalid_column=[-1,31]
    nb_list=[nb for nb in nb_list if nb[0] not in invalid_row and nb[1] not in invalid_column]
    return nb_list

def get_blank_nbs(nb_list):
    blank_nbs=[]
    for item in nb_list:
        if 'blank' in driver.find_element_by_id(f"{str(item[0])}_{str(item[1])}").get_attribute('class'):
            blank_nbs.append(item)
    return blank_nbs
    


driver=webdriver.Chrome()
driver.get("http://minesweeperonline.com/")
def get_every_blank():  
    every_blank_field=driver.find_elements_by_css_selector(".square.blank")
    return every_blank_field

every_blank_field=get_every_blank()


every_blank_field[random.randrange(len(every_blank_field))].click()
time.sleep(1)
def get_every_open():
    every_open_field=driver.find_elements_by_xpath("//*[starts-with(@class, 'square open')]")
    every_open_field=[element for element in every_open_field if 'open0' not in element.get_attribute('class')]
    return every_open_field

def get_bombs_next(item):
    counter=0
    nbs=get_neighbours(item)
    for nb in nbs:
        if 'flagged' in driver.find_element_by_id(f"{str(nb[0])}_{str(nb[1])}").get_attribute('class'):
            counter+=1
    return counter


while(True):
    try:    
        every_open_field=get_every_open()
        for item in every_open_field:
            
            
            if len(get_blank_nbs(get_valid_nbs(get_neighbours(item))))+get_bombs_next(item) == int(item.get_attribute('class')[-1:]):
                bombs=get_blank_nbs(get_valid_nbs(get_neighbours(item)))
                
                for nb in bombs:
                    
                    action = ActionChains(driver)
                    action.context_click(driver.find_element_by_id(f"{str(nb[0])}_{str(nb[1])}")).perform()
                    
                    
                
                every_open_field=get_every_open()
                for item in every_open_field:
                    if get_bombs_next(item) == int(item.get_attribute('class')[-1:]):
                        valid_nbs=get_valid_nbs(get_neighbours(item))
                        for nb in valid_nbs:
                            driver.find_element_by_id(f"{str(nb[0])}_{str(nb[1])}").click()
    except:
        pass
                       
                        
                        
        




    

           

      

            


    