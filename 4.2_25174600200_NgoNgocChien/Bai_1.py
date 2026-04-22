<<<<<<< HEAD
import math
n = int(input("Nhập n: "))
while n <= 0:
    print("n phải là số nguyên dương!")
    n = int(input("Nhập lại n: "))
S1 = 0
for i in range(1, n+1):
    S1 = S1 + i*i
S2 = 0
i = 0
while i <= n:
    so_le = 2*i + 1
    S2 = S2 + so_le**3
    i = i + 1
S3 = 0
for i in range(1, n+1):
    so_chan = 2*i
    S3 = S3 + so_chan**4
S4 = 0
i = 1
while i <= n:
    S4 = S4 + ((-1)**(i-1))/i
    i = i + 1
S5 = 0
for i in range(1, n+1):
    S5 = S5 + 1/(i*(i+1))
S6 = 0
i = 2
while i <= n:
    S6 = S6 + 1/math.sqrt(i)
    i = i + 1
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)
print("S5 =", S5)
=======
import math
n = int(input("Nhập n: "))
while n <= 0:
    print("n phải là số nguyên dương!")
    n = int(input("Nhập lại n: "))
S1 = 0
for i in range(1, n+1):
    S1 = S1 + i*i
S2 = 0
i = 0
while i <= n:
    so_le = 2*i + 1
    S2 = S2 + so_le**3
    i = i + 1
S3 = 0
for i in range(1, n+1):
    so_chan = 2*i
    S3 = S3 + so_chan**4
S4 = 0
i = 1
while i <= n:
    S4 = S4 + ((-1)**(i-1))/i
    i = i + 1
S5 = 0
for i in range(1, n+1):
    S5 = S5 + 1/(i*(i+1))
S6 = 0
i = 2
while i <= n:
    S6 = S6 + 1/math.sqrt(i)
    i = i + 1
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)
print("S5 =", S5)
>>>>>>> 0a506f250e87a8f784abe97ef89d502eff3b202f
print("S6 =", S6)