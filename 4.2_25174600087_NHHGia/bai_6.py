while True:
    n = int(input("Nhập số nguyên n > 100: "))
    if n > 100:
        break
    print("Vui lòng nhập số lớn hơn 100!")
tong = 0
temp_n = n
while temp_n > 0:
    tong += temp_n % 10
    temp_n //= 10
print(f"Tổng các chữ số của {n} là: {tong}")
