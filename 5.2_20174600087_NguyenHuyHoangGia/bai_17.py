# a.
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
ma_tran_A = []
for i in range(m):
    hang = []
    print(f"--- Nhập dữ liệu cho hàng thứ {i + 1} ---")
    for j in range(n):
        gia_tri = int(input(f"Nhập phần tử tại vị trí hàng {i+1}, cột {j+1}: "))
        hang.append(gia_tri)
    ma_tran_A.append(hang)
print("\nMa trận A bạn vừa nhập là:")
for hang in ma_tran_A:
    print(hang)
# b.
tong_tat_ca = 0
for hang in ma_tran_A:
    for gia_tri in hang:
        tong_tat_ca = tong_tat_ca + gia_tri
print("\nTổng tất cả các phần tử trong ma trận A là:", tong_tat_ca)