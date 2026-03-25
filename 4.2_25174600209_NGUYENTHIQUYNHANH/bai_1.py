import math
n = 0
while n <= 0:
    n = int(input("Nhập số nguyên dương n: "))
    if n <= 0:
        print("n phải lớn hơn 0. Vui lòng nhập lại!")
print("-" * 20)
s1 = 0
for i in range(1, n + 1):
    s1 = s1 + i**2
print("a. S1 =", s1)
s2 = 0
for i in range(0, n + 1):
    s2 = s2 + (2*i + 1)**3
print("b. S2 =", s2)
s3 = 0
for i in range(1, n + 1):
    s3 = s3 + (2*i)**4
print("c. S3 =", s3)
s4 = 0
for i in range(1, n + 1):
    s4 = s4 + ((-1)**(i-1)) / i
print("d. S4 =", round(s4, 4))
s5 = 0
for i in range(1, n + 1):
    s5 = s5 + 1 / (i * (i + 1))
print("e. S5 =", round(s5, 4))
s6 = 0
if n >= 2:
    for i in range(2, n + 1):
        s6 = s6 + 1 / math.sqrt(i)
print("f. S6 =", round(s6, 4))

print("-" * 20)