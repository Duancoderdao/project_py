import requests
from bs4 import BeautifulSoup
import re


link_basic = "https://www.bluegrassrealtors.com/index.php?src=directory&view=rets_flex_active_agents&srctype=rets_flex_active_agents_lister&xsearch_id=rets_flex_active_agents_alpha&xsearch=dummy&query=name.starts."
link_domain = "https://www.bluegrassrealtors.com/"

link_list = []

f = open("D:\coder\DATA_ENGINEER\PYTHON\PYTHON\THUC_HANH\craw_data1\list_data.csv", "a")
head = "link_profile,name1,descript, address,phone , email ,\n"
f.write(head)


# lấy ra danh sách
for char in range(65, 91):

    item = link_basic + \
        chr(char) + "&pos=0,1000,1000&xsearch_id=rets_flex_active_agents_alpha&xsearch=dummy"
    link_list.append(item)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


for i in range(len(link_list)):
    print("counter : ", i)
    link = link_list[i]

    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    tr_data = soup.find_all("tr")
    for row in tr_data[1:]:  # [1:] : bỏ đi title và lấy hết các phần đằng sau
        td_list = row.find_all("td")

        # ---- profile
        link_profile = td_list[0].find("a").get('href')
        link_p = link_domain + link_profile

        # ---- name
        name = td_list[1].text.split("\n")  # or get_text()
        name.remove("")
        name1 = name[0].strip().replace(",", "-")
        name2 = name[1].strip().replace(",", "-")

        # -----  address
        address = td_list[2].text.strip().replace(",", "-").replace("\n", " ")

        # ------ constract
        # xử lí phone
        phone = td_list[3].text
        try:
            p = re.compile(r"\([0-9]{3}\)\s+[0-9]{3}\-[0-9]{4}")
            x = p.search(phone)
            pnb = str(x.group(0))
        except:
            pnd = " "

            #    -- email
        try:
            email = td_list[3].find("a").text.strip()
        except:
            email = " "

        str1 = f"{link_p}, {name1}, {name2}, {address}, {pnb},{email}, \n"
        f.write(str1)

f.close()
