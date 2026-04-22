m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
# a
A = []
for i in range(m):
    hang = []
    for j in range(n):
        val = int(input(f"Nhập phần tử A[{i}][{j}]: "))
        hang.append(val)
    A.append(hang)

print("Ma trận A đã nhập:")
for hang in A:
    print(hang)

# b
tong_ma_tran = 0
for hang in A:
    for phan_tu in hang:
        tong_ma_tran += phan_tu

print("Tổng các phần tử của ma trận A là:", tong_ma_tran)