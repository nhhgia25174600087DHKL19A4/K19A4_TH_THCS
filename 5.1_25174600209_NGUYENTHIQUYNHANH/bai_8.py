danh_sach = []
print("Nhập các số nguyên (Nhập 0 để kết thúc):")
while True:
    so = int(input("Nhập số: "))
    if so == 0:
        break  
    danh_sach.append(so)
x = int(input("\nNhập giá trị x cần tìm: "))
tim_thay = False
print(f"Kết quả tìm kiếm cho x = {x}:")
for i in range(len(danh_sach)):
    if danh_sach[i] == x:
        print(f"- Tìm thấy {x} tại vị trí (index): {i}")
        tim_thay = True
if not tim_thay:
    print(f"- Không tìm thấy giá trị {x} trong danh sách.")
print("\nDanh sách em đã nhập là:", danh_sach)