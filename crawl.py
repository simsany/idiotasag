import time
import pyautogui as gui
import pytest
import subprocess

class TestCrawl():
    
    gui.click(gui.locateCenterOnScreen("crawl.png"))
    time.sleep(1)
    hero_x,hero_y=gui.locateCenterOnScreen("hero.png")
    sword_x,sword_y=gui.locateCenterOnScreen("sword.png")
  
    def setup_method(self, method):
       
        self.hero_x,hero_y=gui.locateCenterOnScreen("hero.png")
        self.sword_x,sword_y=gui.locateCenterOnScreen("sword.png")
    
    def test_random(self):
        screen=gui.screenshot(region=(0,0, 1912, 1016))
        crawl=subprocess.Popen(['java', '-jar','D:\\Win10_download\\dungeon-crawl-1.5-WIN.jar'])
        time.sleep(8)
        assert not gui.locateCenterOnScreen(screen)
        
        gui.click(gui.locateCenterOnScreen("crawl.png"))



    def test_there_is_an_item(self):
        assert gui.locateCenterOnScreen("sword.png") or gui.locateCenterOnScreen("key.png") or gui.locateCenterOnScreen("armour.png")
        
    def test_there_is_an_inventory_list(self):
        assert gui.locateCenterOnScreen("inventory.png")



    

    def test_hero_can_stand_on_an_item(self):
        while self.hero_y < self.sword_y:
            
            gui.press('down')
            self.hero_x,self.hero_y=gui.locateCenterOnScreen("hero.png")
            try:
                self.sword_x,self.sword_y=gui.locateCenterOnScreen("sword.png")
            except:
                assert not gui.locateCenterOnScreen("sword.png") and gui.locateCenterOnScreen("hero.png")         
                gui.press('up')
                assert gui.locateCenterOnScreen("sword.png") and gui.locateCenterOnScreen("hero.png")
                gui.click(gui.locateCenterOnScreen("close.png"))

        while self.hero_y > self.sword_y:
            
            gui.press('up')
            self.hero_x,self.hero_y=gui.locateCenterOnScreen("hero.png")
            try:
                self.sword_x,self.sword_y=gui.locateCenterOnScreen("sword.png")
            except:
            
                assert not gui.locateCenterOnScreen("sword.png") and gui.locateCenterOnScreen("hero.png")         
                gui.press('down')
                assert gui.locateCenterOnScreen("sword.png") and gui.locateCenterOnScreen("hero.png")
                gui.click(gui.locateCenterOnScreen("close.png"))


        while self.hero_x < self.sword_x:
        
            gui.press('right')
            self.hero_x,self.hero_y=gui.locateCenterOnScreen("hero.png")
            try:
                self.sword_x,self.sword_y=gui.locateCenterOnScreen("sword.png")
            except:
                assert not gui.locateCenterOnScreen("sword.png") and gui.locateCenterOnScreen("hero.png")         
                gui.press('left')
                assert gui.locateCenterOnScreen("sword.png") and gui.locateCenterOnScreen("hero.png")
                gui.click(gui.locateCenterOnScreen("close.png"))

        while self.hero_x > self.sword_x:
        
            gui.press('left')
            self.hero_x,self.hero_y=gui.locateCenterOnScreen("hero.png")
            try:
                self.sword_x,self.sword_y=gui.locateCenterOnScreen("sword.png")
            except:
                assert not gui.locateCenterOnScreen("sword.png") and gui.locateCenterOnScreen("hero.png")         
                gui.press('right')
                assert gui.locateCenterOnScreen("sword.png") and gui.locateCenterOnScreen("hero.png")
                
     
    def test_hero_can_pick_an_item(self):
        while self.hero_y < self.sword_y:
            
            gui.press('down')
            self.hero_x,self.hero_y=gui.locateCenterOnScreen("hero.png")
            try:
                self.sword_x,self.sword_y=gui.locateCenterOnScreen("sword.png")
            except:
                assert not gui.locateCenterOnScreen("sword.png") and gui.locateCenterOnScreen("hero.png")         
                gui.click(gui.locateCenterOnScreen('pick_up.png'))
                assert gui.locateCenterOnScreen("sword_in_the_list.png") and gui.locateCenterOnScreen("hero.png")
                
                gui.press('up')
                assert not gui.locateCenterOnScreen("sword.png") and gui.locateCenterOnScreen("hero.png")
                gui.click(gui.locateCenterOnScreen("close.png")) 


        while self.hero_y > self.sword_y:
            
            gui.press('up')
            self.hero_x,self.hero_y=gui.locateCenterOnScreen("hero.png")
            try:
                self.sword_x,self.sword_y=gui.locateCenterOnScreen("sword.png")
            except:
            
                assert not gui.locateCenterOnScreen("sword.png") and gui.locateCenterOnScreen("hero.png")         
                gui.click(gui.locateCenterOnScreen('pick_up.png'))
                assert gui.locateCenterOnScreen("sword_in_the_list.png") and gui.locateCenterOnScreen("hero.png")
                
                gui.press('down')
                assert not gui.locateCenterOnScreen("sword.png") and gui.locateCenterOnScreen("hero.png")
                gui.click(gui.locateCenterOnScreen("close.png"))



        while self.hero_x < self.sword_x:
        
            gui.press('right')
            self.hero_x,self.hero_y=gui.locateCenterOnScreen("hero.png")
            try:
                self.sword_x,self.sword_y=gui.locateCenterOnScreen("sword.png")
            except:
                assert not gui.locateCenterOnScreen("sword.png") and gui.locateCenterOnScreen("hero.png")         
                gui.click(gui.locateCenterOnScreen('pick_up.png'))
                assert gui.locateCenterOnScreen("sword_in_the_list.png") and gui.locateCenterOnScreen("hero.png")
             
                gui.press('left')
                assert not gui.locateCenterOnScreen("sword.png") and gui.locateCenterOnScreen("hero.png") 
                gui.click(gui.locateCenterOnScreen("close.png"))

        while self.hero_x > self.sword_x:
        
            gui.press('left')
            self.hero_x,self.hero_y=gui.locateCenterOnScreen("hero.png")
            try:
                self.sword_x,self.sword_y=gui.locateCenterOnScreen("sword.png")
            except:
                assert not gui.locateCenterOnScreen("sword.png") and gui.locateCenterOnScreen("hero.png")         
                gui.click(gui.locateCenterOnScreen('pick_up.png'))
                assert gui.locateCenterOnScreen("sword_in_the_list.png") and gui.locateCenterOnScreen("hero.png")
                
                gui.press('right')
                assert not gui.locateCenterOnScreen("sword.png") and gui.locateCenterOnScreen("hero.png") 
                gui.click(gui.locateCenterOnScreen("close.png"))
                gui.click(gui.locateCenterOnScreen("close.png"))



  
      
    