# đề bài : thêm cột thưởng lương ,  tính tổng lương và xếp loại
       # - sắp xếp tăng dần theo tông lương


# -------------------------------------------
 # encoding = "utf-8-sig" : mode hỗ trợ tiếng việt 
  # mode <r ,w> : phổ biến 

f = open("D:\coder\DATA_ANALYST\PYTHON\THUC_HANH\Them_cot_exel_by_python\Tu_lam\EMPLOYEE.csv" , mode = "r" ,  encoding = "utf-8-sig")

f_new = open("D:\coder\DATA_ANALYST\PYTHON\THUC_HANH\Them_cot_exel_by_python\Tu_lam\EMPLOYEE_new.csv" , mode = "w" ,  encoding = "utf-8-sig")
# lấy hàng tiêu đề
header = f.readline()


# strip() : xóa bỏ khoảng trắng và kí tự thừa 2 bên 
f_new.write(header.strip() + ",Thưởng" + ",Tổng" + ",Xếp loại\n")


 # - lấy hàng nội dung
row = f.readline() # ví như i
 
while row != "" :

        # - split() : cắt thành list bằng dấu ","
       row_list = row.split(",")
        # - ép kiểu : str => float
       salary = float(row_list[2]) 
       

       # - tính thưởng
       bonus = 0
       if salary >= 5000 :
              bonus = 500
       else :
              bonus = 200
       
       # - tính tổng 
       total = salary +  bonus


       # - xếp loại 
       top = total
       rank = ""
       if top >= 5000 :
              rank = "xuất sắc"
       elif top >= 4000 :
              rank = "khá"
       else :
              rank = "Trung bình"
       


       # -render
       row_new = row.strip() + "," + str(bonus) + "," +  str(total) + "," + rank + "\n"
       print(row_new)

   
       f_new.write(row_new)

       row = f.readline() # ví như i++