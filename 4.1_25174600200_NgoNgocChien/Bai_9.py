ID_dung = "chienn"
pass_dung = "992007"
while True:
    ID = input("Nhập ID: ")
    pw = input("Nhập password: ")
    if ID == ID_dung and pw == pass_dung:
        print("Đăng nhập thành công")
        break
    else:
        print("Sai, nhập lại!")