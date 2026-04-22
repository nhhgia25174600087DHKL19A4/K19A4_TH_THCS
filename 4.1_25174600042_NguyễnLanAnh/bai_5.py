n = int(input("Nhập số nguyên: "))

dao = 0
while n != 0:
    chu_so = n % 10
    dao = dao * 10 + chu_so
    n = n // 10

print("Số đảo ngược là: ", dao)