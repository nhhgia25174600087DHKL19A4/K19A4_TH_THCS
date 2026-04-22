n = int(input("Nhập n: "))
A = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    A.append(x)
#a
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("B =", B)
#b
C = [x**2 for x in A]
print("C =", C)
#c
D = [x for x in A if x % 3 == 0]
print("D =", D)