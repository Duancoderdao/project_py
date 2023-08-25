from selenium import webdriver
import pyautogui as pg
from time import sleep

# -  lấy class, id , css ,.. => để auto add text
from selenium.webdriver.common.by import By
   
# from selenium.webdriver.common.keys import Keys


file_user  = open("D:\coder\DATA_ANALYST\PYTHON\THUC_HANH\Auto_like_post/User.txt" , mode = "r")
file_pass = open("D:\coder\DATA_ANALYST\PYTHON\THUC_HANH\Auto_like_post\Pass.txt" , mode = "r")


read_user =  file_user.readline() # as i
read_pass = file_pass.readline()







 #  open Chrome
browser = webdriver.Chrome()
browser.get("https://www.facebook.com/duan.truong.123829/")
sleep(2)
    # user
txt_user = read_user.strip()
pos_user = pg.position(x=485, y=318)
pg.click(pos_user)
pg.write(txt_user)



 # pass
txt_pass = read_pass.strip()
pos_pass = pg.position(x=566, y=390)
pg.click(pos_pass)
pg.write(txt_pass)



# submit
pos_sub = browser.find_element(By.CSS_SELECTOR , "#login_popup_cta_form > div > div:nth-child(5) > div > div")
pos_sub.submit()


# # turn off infor
# sleep(8)
# pos_infor = pg.position(x=500, y=250)
# pg.click(pos_infor)


# cross
sleep(9)
pos_crs = pg.position(x=1042, y=403)
pg.doubleClick(pos_crs)



# like
# pos_like = browser.find_element(By.CLASS_NAME , "x78zum5")
# pos_like.click()truongduan999@gmail.com



sleep(500)



# -----------------
# while read_user != "":
#      #  open Chrome
#     browser = webdriver.Chrome()
#     browser.get("https://www.facebook.com/duan.truong.123829/")
#     sleep(2)
#          # user
#     txt_user = read_user.strip()
#     pos_user = pg.position(x=485, y=318)
#     pg.click(pos_user)
#     pg.write(txt_user)



#       # pass
#     txt_pass = read_pass.strip()
#     pos_pass = pg.position(x=566, y=390)
#     pg.click(pos_pass)
#     pg.write(txt_pass)



#     # submit
#     pos_sub = browser.find_element(By.CSS_SELECTOR , "#login_popup_cta_form > div > div:nth-child(5) > div > div")
#     pos_sub.submit()


#     # # turn off infor
#     # sleep(8)
#     # pos_infor = pg.position(x=500, y=250)
#     # pg.click(pos_infor)


#      # cross
#     sleep(9)
#     pos_crs = pg.position(x=1042, y=403)
#     pg.doubleClick(pos_crs)



#     # like
#     pos_like = browser.find_element(By.CLASS_NAME , "#mount_0_0_H5 > div > div:nth-child(1) > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x5yr21d.x1n2onr6.xh8yej3.x1t2pt76.x1plvlek.xryxfnj > div > div > div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z > div.x78zum5.xdt5ytf.x1t2pt76 > div > div > div.x6s0dn4.x78zum5.xdt5ytf.x193iq5w > div.x9f619.x193iq5w.x1talbiv.x1sltb1f.x3fxtfs.x1swvt13.x1pi30zi.xw7yly9 > div > div.x9f619.x1n2onr6.x1ja2u2z.xeuugli.xs83m0k.x1xmf6yo.x1emribx.x1e56ztr.x1i64zmx.xjl7jj.x19h7ccj.xu9j1y6.x7ep2pv > div:nth-child(3) > div:nth-child(1) > div > div > div > div > div > div > div > div > div > div > div:nth-child(8) > div > div > div:nth-child(4) > div > div > div:nth-child(1) > div > div.xq8finb.x16n37ib > div > div:nth-child(1) > div.x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x3nfvp2.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x5ve5x3 > div.x9f619.x1n2onr6.x1ja2u2z.x78zum5.x1r8uery.x1iyjqo2.xs83m0k.xeuugli.xl56j7k.x6s0dn4.xozqiw3.x1q0g3np.xn6708d.x1ye3gou.xexx8yu.xcud41i.x139jcc6.x4cne27.xifccgj.xn3w4p2.xuxw1ft")
#     pos_like.click()



#     browser.close()
#     read_user =  file_user.readline() # as i+= 1


# sleep(20)



