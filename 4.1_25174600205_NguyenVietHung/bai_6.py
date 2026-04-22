n = int(input("Nhập n: "))
kt = True
if n < 2:
    kt = False
for i in range(2, n):
    if n % i == 0:
        kt = False
        break
print(kt)