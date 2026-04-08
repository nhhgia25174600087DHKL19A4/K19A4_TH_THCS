n = int(input("Nhập bậc n: "))
ma_tran_dv = []

for i in range(n):
    hang = []
    for j in range(n):
        if i == j:
            hang = hang + [1]
        else:
            hang = hang + [0]
    ma_tran_dv = ma_tran_dv + [hang]

for row in ma_tran_dv:
    print(row)