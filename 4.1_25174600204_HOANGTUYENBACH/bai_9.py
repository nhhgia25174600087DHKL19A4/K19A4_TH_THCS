correct_id = "abcd"
correct_pass = "1234"
while True:
    user = input("Nhập ID: ")
    password = input("Nhập password: ")
    if user == correct_id and password == correct_pass:
        print("Đăng nhập thành công!")
        break
    else:
        print("Sai, thử lại")