tu_so = int(input("Nhập tử số: "))
mau_so = 0
while mau_so == 0:
    mau_so = int(input("Nhập mẫu số (phải khác 0): "))
    if mau_so == 0:
        print("Mẫu số không thể bằng 0. Vui lòng nhập lại!")
print("-" * 20)
print(f"Phân số bạn đã nhập là: {tu_so}/{mau_so}")
if tu_so == 0:
    print("Giá trị của phân số bằng: 0")
else:
    print("Giá trị của phân số xấp xỉ:", round(tu_so / mau_so, 4))
print("-" * 20)
