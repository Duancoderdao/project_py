
'''
  Tức là với chiêu này ta có thể “khóa” 1 đoạn code trong file chính lại
khi nó được import bởi một file khác.
Đoạn code bị khóa đó chỉ chạy khi file chính
được mở trực tiếp: = > có thể tái sử dụng hàm trong file chính
và test hàm thẳng từ trong module
mà không sợ ảnh hưởng kết quả khi chạy file chính(có import cái module đó)
'''

if __name__ == "__main__":
    # hàm chạy
    main()
