tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
while mau == 0:
    print("Mẫu số phải khác 0!")
    mau = int(input("Nhập lại mẫu số: "))
print("Phân số vừa nhập là:", tu, "/", mau)
gia_tri = tu / mau
print("Giá trị của phân số =", gia_tri)