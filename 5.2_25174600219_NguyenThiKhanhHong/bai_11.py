import random
n = int(input("Nhập số lượng phần tử n: "))
A = []
for i in range(n):
    A.append(int(input(f"Nhập phần tử thứ {i+1}: ")))
# a. 
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("Danh sách B (chia hết cho 3, không cho 5):", B)
# b. 
C = [x**2 for x in A]
print("Danh sách C (bình phương của A):", C)
# c.
chia_het_cho_3 = [x for x in A if x % 3 == 0]
if len(chia_het_cho_3) > 0:
    D = [x for x in random.sample(chia_het_cho_3, min(len(chia_het_cho_3), 3))]
    print("Danh sách D (ngẫu nhiên từ các số chia hết cho 3):", D)
else:
    print("Danh sách A không có số nào chia hết cho 3 để tạo D.")