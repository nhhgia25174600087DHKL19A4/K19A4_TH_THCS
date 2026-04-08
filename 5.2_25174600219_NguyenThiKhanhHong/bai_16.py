n = int(input("Nhập bậc n của ma trận đơn vị: "))
ma_tran_dv = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
print(f"Ma trận đơn vị bậc {n}:")
for hang in ma_tran_dv:
    print(hang)