n = int(input("Nhập số n (bậc ma trận): "))

ma_tran_don_vi = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

print("\nMa trận đơn vị bậc", n, ":")
for hang in ma_tran_don_vi:
    print(hang)