print("Hãy nhập các số dương (Nhập một số âm để dừng lại):")
danh_sach_so = []
while True:
    so = float(input("Nhập một số: "))
    if so < 0:
        print("Bạn đã nhập số âm. Chương trình kết thúc.")
        break 
    danh_sach_so.append(so)
    print(f"Số vừa nhập: {so}")
print("Các số dương bạn đã nhập là:", danh_sach_so)