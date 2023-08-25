
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys


videoFileName = "D:\coder\DATA_ANALYST\PYTHON\THUC_HANH\cay_view\list_url_video.txt"
btPlaySelecter = "#movie_player > div.ytp-cued-thumbnail-overlay > button"
viewFileCount = "D:\coder\DATA_ANALYST\PYTHON\THUC_HANH\cay_view\\viewCout.txt"


videoFile = open(videoFileName)
listsVideo = videoFile.readlines()



NUMBER_OF_TAB = 4
NUMBER_OF_VIDEO = len(listsVideo)
LOOP_TIME = 3





videoIndex = 0
tabIndex = 0
tabCount = 1
viewCout = 0


 # - open browser
browser = webdriver.Chrome()

 # - open url lst = tabIndex = 0

browser.get(listsVideo[videoIndex])



  # - click play button
sleep(2)
playButton = browser.find_element(By.CSS_SELECTOR ,btPlaySelecter)
playButton.click()




while  True:
   videoIndex = (videoIndex + 1) % NUMBER_OF_VIDEO
   tabIndex = (tabIndex + 1) % NUMBER_OF_TAB

   if tabCount < NUMBER_OF_TAB:
     
      tabCount = tabCount + 1

      browser.execute_script("window.open('"+listsVideo[videoIndex].strip()+"')")
      
 

   else :
      browser.switch_to.window(browser.window_handles[tabIndex])
      sleep(2)
      browser.get(listsVideo[videoIndex])
   
   viewCout = viewCout + 1
   saveFile = open(viewFileCount , mode = "w")
   saveFile.write(str(viewCout))
   saveFile.close()


   sleep(LOOP_TIME)

sleep(80)




















