n = int(input("Nhập số: "))
dau = 1
if n < 0:
    dau = -1
    n = -n
dao = 0
while n != 0:
    dao = dao * 10 + n % 10
    n //= 10
print("Số đảo:", dao * dau)