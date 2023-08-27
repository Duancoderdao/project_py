from code_process import email_process


def main():

    f = open("D:\coder\DATA_ANALYST\PYTHON\THUC_HANH\\tach_user&domen_email\input.txt",
             "r", encoding="UTF-8")
    w = open("D:\coder\DATA_ANALYST\PYTHON\THUC_HANH\\tach_user&domen_email\output.csv",
             "w", encoding="UTF-8")
    read_text = f.readlines()

    header_new = "User_name" + "," + "domain_name" + "\n"
    w.write(header_new)

    for i in read_text:
        user, domain = email_process(i)
        row_new = user.strip() + "," + domain.strip() + "\n"
        w.write(row_new)


if __name__ == "__main__":
    main()
