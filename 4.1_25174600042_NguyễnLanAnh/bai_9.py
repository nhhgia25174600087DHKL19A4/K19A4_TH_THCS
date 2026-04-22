user = "admin"
pw = "123456789"

while True:
    id = input("Nhập ID: ")
    password = input("Nhập password: ")

    if id == user and password == pw:
        print("Đăng nhập thành công!")
        break
    else:
        print("Sai. Nhập lại!")