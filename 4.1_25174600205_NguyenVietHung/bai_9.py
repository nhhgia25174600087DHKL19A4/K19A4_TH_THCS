while True:
    id = input()
    pw = input()

    if id == "admin" and pw == "123":
        print("Đúng")
        break

    print("Sai")