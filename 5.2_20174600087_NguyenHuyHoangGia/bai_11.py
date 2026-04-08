n = int(input("Nhập số lượng phần tử n cho danh sách A: "))
A = []
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i+1}: "))
    A.append(so)
print("Danh sách A ban đầu:", A)
# a.
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("Danh sách B (chia hết cho 3, không chia hết cho 5):", B)
# b.
C = [x**2 for x in A]
print("Danh sách C (bình phương của A):", C)
# c.
A_chia_het_cho_3 = [x for x in A if x % 3 == 0]
D = []
if len(A_chia_het_cho_3) > 0:
    vi_tri_ngau_nhien = id(A) % len(A_chia_het_cho_3)
    so_ngau_nhien = A_chia_het_cho_3[vi_tri_ngau_nhien]
    D.append(so_ngau_nhien)
    print("Danh sách D:", D)
else:
    print("Danh sách A không có số nào chia hết.")