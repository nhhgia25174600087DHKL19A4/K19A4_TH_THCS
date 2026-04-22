while True:
    tu = int(input("Nhập tử số: "))
    mau = int(input("Nhập mẫu số: "))
    if mau != 0:
        break
    print("Mẫu phải khác 0, nhập lại!")
print("Phân số là:", tu, "/", mau)