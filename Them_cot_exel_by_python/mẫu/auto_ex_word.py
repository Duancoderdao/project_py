  # -  encoding = "utf-8-sig" : mode hỗ trợ tiếng việt có dấu
     # - read : đọc nhiều dòng 
     # - readline : đọc 1 dòng
file = open("D:\coder\DATA_ANALYST\PYTHON\THUC_HANH\Them_cot_exel_by_python\mẫu\students.csv", mode = "r", encoding = "utf-8-sig")

 # -- tạo 1 file mới để viết vào 
file_new = open("D:\coder\DATA_ANALYST\PYTHON\THUC_HANH\Them_cot_exel_by_python\mẫu\students_new.csv", mode = "w", encoding = "utf-8-sig")
header = file.readline()
 # -- strip() : xóa bỏ khoảng trắng và kí tự thừa 2 bên 
file_new.write(header.strip() + ",Điểm trung bình,Học lực\n")


  # -- đọc 1 dòng trước rùi kiểm tra while 
row = file.readline() # ví như i

while row != "":
   
      # - split => cắt chuỗi bởi dấu chấm phẩy => 1 new list 
   row_list = row.split(",")

    # -- lấy ra điểm toán và văn <> ép kiểu từ str sang float
   toan = float(row_list[2])
   van = float(row_list[3])

   ave = (toan + van )/ 2
   # -- làm tròn 1 số 
   ave = round(ave,1)

   rank = ""
   if ave > 8.0 :
      rank = "Gioi"
   elif ave > 6.5 :
      rank = "Tiên tiến"
   elif ave < 6.5 :
      rank = "Trung bình"
   else :
      rank = "Yếu"


   row_new = row.strip() + "," + str(ave) + "," + rank + "\n"
   print(row_new)

   file_new.write(row_new)
    
   
   row = file.readline() # ví như i++
   print("-------------" + row) 
 