while True:
    n = int(input("Nhập số > 100: "))
    if n > 100:
        break
    print("Nhập lại!")
tong = 0
while n > 0:
    tong += n % 10
    n //= 10
print("Tổng chữ số =", tong)