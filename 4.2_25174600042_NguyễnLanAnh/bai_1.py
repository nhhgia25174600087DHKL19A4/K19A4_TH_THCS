import math
n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n (>0): "))
#a
S1_for = sum(i**2 for i in range(1, n+1))

S1_while = 0
i = 1
while i <= n:
    S1_while += i**2
    i += 1
#b
S2_for = sum((2*i + 1)**3 for i in range(n+1))

S2_while = 0
i = 0
while i <= n:
    S2_while += (2*i + 1)**3
    i += 1
#c
S3_for = sum((2*i)**4 for i in range(1, n+1))

S3_while = 0
i = 1
while i <= n:
    S3_while += (2*i)**4
    i += 1
#d
S4_for = sum(((-1)**(i-1)) / i for i in range(1, n+1))

S4_while = 0
i = 1
while i <= n:
    S4_while += ((-1)**(i-1)) / i
    i += 1
#e
S5_for = sum(1/(i*(i+1)) for i in range(1, n+1))

S5_while = 0
i = 1
while i <= n:
    S5_while += 1/(i*(i+1))
    i += 1
#f
S6_for = sum(1/math.sqrt(i) for i in range(2, n+1))

S6_while = 0
i = 2
while i <= n:
    S6_while += 1/math.sqrt(i)
    i += 1

print("S1:", S1_for, S1_while)
print("S2:", S2_for, S2_while)
print("S3:", S3_for, S3_while)
print("S4:", S4_for, S4_while)
print("S5:", S5_for, S5_while)
print("S6:", S6_for, S6_while)