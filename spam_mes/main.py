import pyautogui as pg
import time
import pyperclip

time.sleep(3)


txt = open("D:\coder\DATA_ANALYST\PYTHON\THUC_HANH\spam_mes\content.txt" , mode = "r" , encoding = "utf-8")


for i in txt :
	str = i
	pyperclip.copy(str)
	pg.hotkey("ctrl", "v")
	pg.press("Enter")
	time.sleep(1)
	


# ------------------------


	
	
