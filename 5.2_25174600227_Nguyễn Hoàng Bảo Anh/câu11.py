n = int(input("Nhập n: "))
A = []
for i in range(n):
    A = A + [int(input(f"Nhập A[{i}]: "))]
# a.
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("Danh sách B:", B)

# b.
C = [x * x for x in A]
print("Danh sách C:", C)