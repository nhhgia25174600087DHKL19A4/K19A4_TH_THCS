import random
n = int(input("Nhập n: "))
A = []
for i in range(n):
    while True:
        x = random.randint(1, 99999)
        if x % 7 != 0:
            A += [x]
            break
print("Danh sách A:")
print(A)