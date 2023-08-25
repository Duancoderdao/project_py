import pyautogui as pg 
from time import sleep

#     # ---------------lý thuyết -----------------
# # pyautogui : 
#    # - thực hiện thao tác trực tiếp lêm màn hình máy tính 
#    # - không thực hiện trên webbdriver như selenium đc
#    # - tự thực hiện các tác vụ khi nhấn keyboard
#    # - khi thu nhỏ hoặc di chuyển màn hình thì sẽ mất đi vị trí ban đầu


#  #1.Tìm tọa độ

# """

# screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
# currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
# pyautogui.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.
# pyautogui.click() # Click the mouse at its current location.
# pyautogui.click(200, 220) # Click the mouse at the x, y coordinates 200, 220.
# pyautogui.move(None, 10)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
# pyautogui.doubleClick() # Double click the mouse at the
# pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad) # Use tweening/easing function to move mouse over 2 seconds.
# pyautogui.write('Hello world!', interval=0.25)  # Type with quarter-second pause in between each key.
# pyautogui.press('esc') # Simulate pressing the Escape key.
# pyautogui.keyDown('shift')
# pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left'])
# pyautogui.keyUp('shift')
# pyautogui.hotkey('ctrl', 'c')

# """


#  #2.Hiển thị thông báo 

#            # - thông báo 
#    #  >>> pyautogui.alert('This is an alert box.') 
  
#             # gửi xác nhận
#    #  >>> pyautogui.confirm('Shall I proceed?')
   

#            # gửi xác nhận có điều kiện 
#    #  >>> pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
  

#           # thông báo và có ô input nhập
#    #  >>> pyautogui.prompt('What is your name?')
   


#    #  >>> pyautogui.password('Enter password (text will be hidden)')
#    #  'swordfish'









# # -------------------THỰC HÀNH ------------------


#   # VD1 : nhập input và sẽ thông báo ra màn hình


# # infor = pg.confirm("Bạn có yêu a duẩn đẹp zai không ! " , buttons = ["Có ", "Không"])

# # if(infor.strip() == "Có"):
# # 	pg.alert("yêu em nhiều")
# # else :
# # 	pg.alert(" đồ phụ tình ")



 
#   # VD 2: tìm tọa độ và auto click
# # i = 0
# # while i < 4:
# # 	# tìm tọa độ
# # 	pos = pg.position(x=1076, y=14)
# # 	print(pos)
# # 	 # auto click
# # 	pg.click(pos)
# # 	i+=1


#    # VD3: tự động refesh mỗi lần , cày view youtube

# i = 0
# while i < 4:
# 	pos = pg.position(x=106, y=57)
# 	print(pos)
# 	pg.click(pos)
# 	sleep(30)
# 	i+= 1



# VD4 : TỰ ĐỘNG LIKE ON FACEBOOK bằng 
   

  # CÁCH 1 : DÙNG position
# pos = pg.position(x=532, y=580)
# print(pos)
# pg.click(pos)


   # CÁCH 2 : locateOnScreen<tìm kiếm bằng đối tượng>

# sleep(2)
# imgage = 'D:\coder\DATA_ANALYST\PYTHON\THUC_HANH\Auto_click_pygui\like.png'
# loc = pg.locateOnScreen(imgage)
# print(loc)
# pg.click(loc)



  # VD5 : AUTO tym và chuyển video

for _ in range(100):
	pos_tym = pg.position(x=500, y=396)
	pg.doubleClick(pos_tym)
	sleep(4)
	pos_next = pg.position(x=777, y=401) 
	pg.click(pos_next)



 # VD6.
# print("hello")