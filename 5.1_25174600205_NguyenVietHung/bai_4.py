while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))

    if 0 < m < n:
        break
    else:
        print("Lỗi, nhập lại!")

lst = [0] * 100
count = 0
i = m

while i <= n and count < 100:
    lst[count] = i
    count += 1
    i += 2

tong = 0
for i in range(count):
    tong += lst[i]

print("Tổng là:", tong)