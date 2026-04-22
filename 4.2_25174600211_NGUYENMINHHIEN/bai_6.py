while True:
    n_str = input("Nhập số > 100: ")
    n = int(n_str)
    if n > 100:
        break
    print("Số phải lớn hơn 100!")
tong = 0
for chu_so in n_str:
    tong += int(chu_so)
print(f"Tổng các chữ số: {tong}")