n = int(input("Nhập số lớn hơn 100: "))

while n <= 100:
    n = int(input("Nhập lại số lớn hơn 100: "))
tong = 0

while n > 0:
    tong += n % 10
    n //= 10

print("Tổng các chữ số là: ", tong)



































































