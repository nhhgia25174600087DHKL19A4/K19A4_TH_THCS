id_dung = "admin"
pass_dung = "123"
while True:
    user_id = input("Nhập ID: ")
    user_pass = input("Nhập Password: ")   
    if user_id == id_dung and user_pass == pass_dung:
        print("Đăng nhập thành công!")
        break
    else:
        print("Sai ID hoặc Password, vui lòng thử lại.")