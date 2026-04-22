import random
n = int(input("Nhập số phần tử n: "))
A = []

for i in range(n):
    x = int(input(f"Nhập A[{i}]: "))
    A.append(x)

# a
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("Danh sách B:", B)

# b
C = [x * x for x in A]
print("Danh sách C:", C)

# c
temp = [x for x in A if x % 3 == 0]

D = []
if len(temp) > 0:
    for i in range(len(temp)):
        # chọn ngẫu nhiên từ temp
        D.append(temp[random.randint(0, len(temp) - 1)])

print("Danh sách D:", D)