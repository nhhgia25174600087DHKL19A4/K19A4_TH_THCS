n = int(input("Nhập bậc của ma trận đơn vị n: "))
ma_tran_don_vi = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
print(f"Ma trận đơn vị bậc {n}:")
for hang in ma_tran_don_vi:
    print(hang)