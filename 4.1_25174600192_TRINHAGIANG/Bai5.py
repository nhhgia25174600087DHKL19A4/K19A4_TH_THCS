n = int(input("Nhập một số nguyên: "))

so_dao = 0
tam = abs(n)

while tam > 0:
    chu_so = tam % 10
    so_dao = so_dao * 10 + chu_so
    tam = tam // 10

if n < 0:
    so_dao = -so_dao

print("Số đảo ngược là:", so_dao)