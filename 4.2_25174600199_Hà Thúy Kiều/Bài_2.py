tu = int(input("Nhập tử: "))
mau = int(input("Nhập mẫu: "))
while mau == 0:
    print("Mẫu phải khác 0!")
    mau = int(input("Nhập lại mẫu: "))
print("Phân số:", tu, "/", mau)