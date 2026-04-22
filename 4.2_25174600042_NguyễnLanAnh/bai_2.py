tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))

while mau == 0:
    print("Mẫu số phải khác 0!")
    mau = int(input("Nhập lại mẫu số: "))

print("Phân số là:", tu, "/", mau)