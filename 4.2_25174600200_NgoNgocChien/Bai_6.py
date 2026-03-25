n = int(input("Nhập số > 100: "))
while n <= 100:
    print("Số phải lớn hơn 100")
    n = int(input("Nhập lại: "))
tong = 0
while n > 0:
    chu_so = n % 10
    tong = tong + chu_so
    n = n // 10
print("Tổng các chữ số =", tong)