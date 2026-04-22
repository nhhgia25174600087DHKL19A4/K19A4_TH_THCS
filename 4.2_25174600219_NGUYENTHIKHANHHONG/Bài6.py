#Dùng while
n = int(input("Nhập n (>100): "))

while n <= 100:
    n = int(input("Nhập lại n (>100): "))

tong = 0

while n > 0:
    tong += n % 10
    n //= 10

print("Tổng chữ số là:", tong)

#Dùng for
n = input("Nhập n (>100): ")

while int(n) <= 100:
    n = input("Nhập lại n (>100): ")

tong = 0

for i in n:
    tong += int(i)

print("Tổng chữ số là:", tong)