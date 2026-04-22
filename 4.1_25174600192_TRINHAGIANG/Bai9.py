id_dung = "admin"
mat_khau_dung = "123"

while True:
    user_id = input("Nhập ID: ")
    password = input("Nhập password: ")
    
    if user_id == id_dung and password == mat_khau_dung:
        print("Đăng nhập thành công!")
        break
    else:
        print("Sai ID hoặc password, nhập lại!")