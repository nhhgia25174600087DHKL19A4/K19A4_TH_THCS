ID_dung = "admin"
pass_dung = "123"

while True:
    id = input("Nhap ID: ")
    pw = input("Nhap password: ")

    if id == ID_dung and pw == pass_dung:
        print("Đang nhap thanh cong!")
        break
    else:
        print("Sai, nhap lai!")