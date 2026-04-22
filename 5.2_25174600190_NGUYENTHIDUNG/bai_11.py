n = int(input("Nhập số lượng phần tử n: "))
A = []
for i in range(n):
    val = int(input(f"Nhập phần tử A[{i}]: "))
    A.append(val)
# a
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("Danh sách B:", B)
# b
C = [x**2 for x in A]
print("Danh sách C:", C)

# c
D = [x for x in A if x % 3 == 0]
print("Danh sách D (các số chia hết cho 3 từ A):", D)