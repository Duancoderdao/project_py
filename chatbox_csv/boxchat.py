
import csv
f = open('D:\coder\DATA_ANALYST\PYTHON\THUC_HANH\chatbox_csv\chatbox.csv')
reader = csv.reader(f)


data = {}

name = input("BOT : What's your name ? \n")
print("BOT : hello", name)
print("----------------")

# read file and loop => save into dictionary
# '''
#   two 2 situation :
#    situation 1 :
#      - nếu đọc trực tiếp bằng file nó sẽ đọc đủ số lượng chiều dài của file
#          ,và không quay lại từ đầu đọc lại đc

#    situation 2:
#     - lưu data vào 1 dict thì nó sẽ có thể lặp hết vòng và có thể bắt đầu lại được
# '''
for question, answer in reader:
    data[question] = answer


while True:

    isSuccess = False

    print("BOT : What information do you want to know  ?  ")
    question_from_user = input(f"{name} : ")

    # data.keys() : take keys from dict
    for question in data.keys():

        if question in question_from_user:
            result = data[question]
            print("BOT :", result, "\n")
            isSuccess = True

    if isSuccess == False:
        print("BOT : Sorry , i don't understand your question ! \n")
    #  exit program
    print("BOT : Do you want to ask other questions ? : (yes , no) ")
    pause = input()
    print("\n")
    if pause == 'no':
        break
