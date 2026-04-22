n = int(input("Nhập số lượng phần tử của danh sách A: "))
A = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]
print("\nDanh sách A:", A)

# a
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("\nDanh sách B:", B)

# b
C = [x**2 for x in A]
print("\nDanh sách C:", C)

# c
D = [x for x in A if x % 3 == 0]
print("\nDanh sách D:", D)