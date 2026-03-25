n = int(input("Nhập một số nguyên: "))
so_dao_nguoc = 0
tam = abs(n)
while tam > 0:
    chu_so = tam % 10
    so_dao_nguoc = so_dao_nguoc * 10 + chu_so
    tam = tam // 10
if n < 0:
    print(f"Số đảo ngược là: -{so_dao_nguoc}")
else:
    print(f"Số đảo ngược là: {so_dao_nguoc}")