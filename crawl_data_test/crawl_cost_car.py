import requests
from bs4 import BeautifulSoup


link_basic = 'https://dailymuabanxe.net/gia-xe-audi'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(link_basic, headers=headers)
f = open('D:\coder\DATA_ENGINEER\PYTHON\PYTHON\THUC_HANH\crawl_data_test\cost_car.csv',
         'w', encoding='utf-8')
if r.status_code == 200:
    soup = BeautifulSoup(r.content, 'html.parser')
    head = "name , cost , \n"
    f.write(head)
    #  lấy table bảng giá  đầu tiên
    link_table = soup.find("table")
    # từ table lấy tất cả những thẻ tr, td trong table đó
    links = link_table.find_all("tr")
    for data in links[1:]:
        data_detail = data.find_all("td")

        # name car
        name_car = data_detail[0].find("strong").get_text().strip()
        cost_car = data_detail[1].find(
            "span").get_text().strip().replace(".", "")

        # -- viết vào file
        w_file = f'{name_car}, {cost_car} , \n'
        f.write(w_file)
f.close
