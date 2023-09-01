import requests
from bs4 import BeautifulSoup


#  phòng  nhiều web sẽ bắt xác nhận có phải robot hay không
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
f = open('D:\coder\DATA_ENGINEER\PYTHON\PYTHON\THUC_HANH\craw_data_article\list_data_article.csv',
         'w', encoding='utf-8')

r = requests.get("https://dantri.com.vn",  headers=headers)
head = "link_img , title  \n"
f.write(head)
# #  lấy data trên web về
# # - text : lấy mỗi chữ
# # - content : lấy cả hình ảnh ,...
# # - json() : lấy kiểu dạng json


if r.status_code == 200:
    # kiểm tra trạng thái : json or status_code => 200 -> success , 400 -> false
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.find_all("article")
    i = 1
    for row in data:

        print("counter : ", i)
        #  --------- img
        link_img = "https://dantri.com.vn" + \
            row.find('a').get('href').strip()

    #  ----- title
        # method BeautifulSoup  : text = get_text()
        title = row.find('h3').get_text().strip().replace("\n", ' ')

        # result
        file_csv = f'{link_img}, {title} , \n'
        f.write(file_csv)
        i += 1
else:
    print("Không tìm thấy đường link ")

f.close
