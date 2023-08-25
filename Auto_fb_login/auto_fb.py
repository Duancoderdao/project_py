
from time import sleep
from selenium import webdriver
 # - để define By khi tìm element
  # - We use the By class to specify which attribute is used to locate elements on the page.
from selenium.webdriver.common.by import By
  # - dùng để submit 
from selenium.webdriver.common.keys import Keys

# - chưa bt dùng thế nào 
# from selenium.webdriver.chrome.service import Service




Index = 0


 # mở file
file_user = open("D:\coder\DATA_ANALYST\PYTHON\THUC_HANH\Auto_fb_login\\user.txt" , mode = "r" , encoding = "utf-8")
file_pass = open("D:\coder\DATA_ANALYST\PYTHON\THUC_HANH\Auto_fb_login\pass.txt" , mode = "r" , encoding = "utf-8")


# đọc file
read_user = file_user.readline() #i
read_pass = file_pass.readline() #j





while read_user != "":

     # mở Chrome
    browser = webdriver.Chrome()
    # chạy chrome
    browser.get("https://www.facebook.com/duan.truong.123829/")



    # while read_user != "":
    # tài khoản
      # + lấy id input
    txtUser = browser.find_element(By.ID, "email")
      # + nhập vào input
        # + send_keys : thêm giá trị vào input
    txtUser.send_keys(read_user.strip())



    # mật khẩu 
      # + lấy id of input
    txtPass = browser.find_element(By.ID, "pass")
        # + nhập vào input
        # + send_keys : thêm giá trị vào input
         # + strip() : xóa khoảng trắng hoặc kí tự để không bị nhảy xuống ô submit
    txtPass.send_keys(read_pass.strip())




    # sign in 
    # txtPass.submit()
     # - or
    txtPass.send_keys(Keys.ENTER)
    sleep(1)
    


    read_user = file_user.readline()  #i++
    read_pass = file_pass.readline()  #j++

    # - end the program
    sleep(3)
    browser.close()
    sleep(3)
   


