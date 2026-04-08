m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))

A = []
for i in range(m):
    hang = []
    for j in range(n):
        gia_tri = int(input(f"Nhập phần tử A[{i+1}][{j+1}]: "))
        hang.append(gia_tri)
    A.append(hang)

print("\nMa trận A:")
for hang in A:
    print(hang)
#b
tong = 0
for hang in A:
    for gia_tri in hang:
        tong += gia_tri

print("\nTổng các phần tử của ma trận A:", tong)