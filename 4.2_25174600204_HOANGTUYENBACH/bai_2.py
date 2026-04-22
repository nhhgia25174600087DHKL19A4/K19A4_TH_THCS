tu = int(input("Nhập tử số: "))
while True:
    mau = int(input("Nhập mẫu số (≠ 0): "))
    if mau != 0:
        break
    print("Mẫu phải khác 0, nhập lại!")
print("Phân số là:", tu, "/", mau)