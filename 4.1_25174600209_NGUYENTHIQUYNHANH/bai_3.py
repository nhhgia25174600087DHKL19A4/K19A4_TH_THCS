a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
tich = 0
while b > 0:
    if b % 2 != 0:
        tich = tich + a
    a = a + a
    b = b // 2
print(f" kết quả là: {tich}")    