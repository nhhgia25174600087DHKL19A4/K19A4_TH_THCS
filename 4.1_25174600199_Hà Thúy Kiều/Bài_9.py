ID_DUNG = "hathuykieu"
PASS_DUNG = "12345"
while True:
    user = input("Nhập ID: ")
    password = input("Nhập password: ")
    if user == ID_DUNG and password == PASS_DUNG:
        print("Đăng nhập thành công!")
        break
    else:
        print("Sai ID hoặc password, vui lòng nhập lại!")