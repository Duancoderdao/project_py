
#  ==> viết kiểu này sau sẽ có thể tái sử dụng đc


def email_process(email):
    email_user = email[0:email.index("@")]
    email_domain = email[email.index("@") + 1:]
    return email_user, email_domain


def output(email_user, email_domain):

    print(f"email_user : {email_user}")
    print(f"email_domain : {email_domain}")
    print()


def main():
    email = input("Vui lòng nhập địa chỉ email : \n")
    email_user, email_domain = email_process(email)
    output(email_user, email_domain)


if __name__ == "__main__":
    main()
