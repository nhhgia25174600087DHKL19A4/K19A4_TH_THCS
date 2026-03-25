ID_DUNNG = "admin"
PASS_DUNG = "12345"
while True:
    user_id = input("Nhập ID: ")
    user_pass = input("Nhập Password: ")
    if user_id == ID_DUNNG and user_pass == PASS_DUNG:
        print("Đăng nhập thành công!")
        break
    else:
        print("Sai ID hoặc Password. Vui lòng thử lại.")