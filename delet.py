import keyboard
import time
import pyautogui
def delet():
      
        time.sleep(2)
        for _ in range(80):
                

                pyautogui.click(306,859,button='right')
                time.sleep(2)
                try:
                        h= pyautogui.locateOnScreen('csett.png', confidence=0.80)
                        h =pyautogui.center(h)
                        x,y=h
                        time.sleep(2)
                        pyautogui.click(x,y)
                        time.sleep(2)
                        h= pyautogui.locateOnScreen('dell.png', confidence=0.80)
                        h =pyautogui.center(h)
                        x,y=h
                        time.sleep(2)
                        pyautogui.click(x,y)
                        time.sleep(2)
                        continue
                except:
                
                        pyautogui.click(312,830)
                        time.sleep(2)
                        pyautogui.click(1134,586)
                        time.sleep(2)
