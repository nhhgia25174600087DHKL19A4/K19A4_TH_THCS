import random
n = int(input("Nhập n: "))
A = list(map(int, input("Nhập các phần tử: ").split()))
#a.
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("a) B =", B)

#b.
C = [x**2 for x in A]
print("b) C =", C)

#c.
D = [x for x in A if x % 3 == 0]
if len(D) > 0:
    kq = random.choice(D)
    print("c) Phần tử ngẫu nhiên chia hết cho 3:", kq)
else:
    print("c) Không có phần tử chia hết cho 3")