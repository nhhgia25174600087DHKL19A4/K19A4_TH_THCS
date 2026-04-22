id_dung = "admin"
mk_dung = "123"
while True:
    user = input("Nhap ID: ")
    mk = input("Nhap password: ")
    if user == id_dung and mk == mk_dung:
        print("Dung roi")
        break
    else:
        print("Sai, nhap lai")