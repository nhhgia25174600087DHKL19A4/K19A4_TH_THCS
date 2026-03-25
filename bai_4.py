print("Nhập các số dương (nhập số âm để dừng):")
while True:
    n = float(input("Nhập một số: "))
    if n < 0:
        print("Đã nhập số âm. Kết thúc chương trình.")
        break
    print(f"Số vừa nhập: {n}")  