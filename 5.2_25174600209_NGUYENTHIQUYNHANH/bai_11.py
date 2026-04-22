n = int(input("Nhập số lượng phần tử n: "))
A = []
for i in range(n):
    so = int(input(f"Nhập phần tử thứ {i+1}: "))
    A.append(so)
print(f"\nDanh sách A đã nhập: {A}")
B = []
for x in A:
    if x % 3 == 0 and x % 5 != 0:
        B.append(x)
print(f"a. Danh sách B (chia hết cho 3, không chia cho 5): {B}")
C = []
for x in A:
    binh_phuong = x * x
    C.append(binh_phuong)
print(f"b. Danh sách C (Bình phương của A): {C}")
D = []
for x in A:
    if x % 3 == 0:
        D.append(x)
if len(D) >= 2:
    D_ngau_nhien = [D[0], D[-1]]
    print(f"c. Danh sách D (Lấy vài số chia hết cho 3): {D_ngau_nhien}")
else:
    print(f"c. Danh sách D: {D}")