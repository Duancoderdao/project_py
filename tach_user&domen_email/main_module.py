from code_process import email_process, output


def main():
    emails = ["ayeume@gmail.com",
              "truognduan999@gmail.vn", "quengochai@gmail.edu"]
    for email in emails:
        print(email)
        user, domain = email_process(email)
        output(user, domain)


if __name__ == "__main__":
    main()
