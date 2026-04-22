while True:
    x = input("Nhập ID: ")
    y = input("Nhập password: ")
    if x == "admin" and y == "123":
        print("Đúng rồi!")
        break
    else:
        print("Sai, nhập lại!")