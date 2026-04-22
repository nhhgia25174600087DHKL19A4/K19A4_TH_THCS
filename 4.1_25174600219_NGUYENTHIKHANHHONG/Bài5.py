n = int(input("Nhập số nguyên: "))
m = 0
s = abs(n)
while s > 0:
    m = m * 10 + s% 10
    s = s // 10
if n < 0:
    m = -m
print("Số đảo ngược:", m)