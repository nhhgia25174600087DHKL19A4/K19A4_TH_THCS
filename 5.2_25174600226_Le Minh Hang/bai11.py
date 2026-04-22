import random

n = int(input("Nhập n: "))
A = [int(input(f"A[{i}]: ")) for i in range(n)]

# a. chia hết cho 3 nhưng không chia hết cho 5
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("a. B =", B)

# b. bình phương
C = [x**2 for x in A]
print("b. C =", C)

# c. phần tử ngẫu nhiên chia hết cho 3
D = [random.choice([x for x in A if x % 3 == 0]) for i in range(n) if any(x % 3 == 0 for x in A)]
print("c. D =", D)