n = 0
while n <= 0:
    n = int(input("nhap so nguyen duong "))
    if n <= 0:
        print("loi")
s1 = 0
for i in range(1, n + 1):
    s1 += i * i
s2 = 0
for i in range(0, n + 1):
    s2 += (2*i + 1)**3
s3 = 0
for i in range(1, n + 1):
    s3 += (2*i)**4
s4 = 0
for i in range(1, n + 1):
    mau = i
    tu = 1 if (i - 1) % 2 == 0 else -1
    s4 += tu / mau
s5 = 0
for i in range(1, n + 1):
    s5 += 1 / (i * (i + 1))
s6 = 0
for i in range(2, n + 1):
    s6 += 1 / (i ** 0.5)
print(f"S1 = {s1}\nS2 = {s2}\nS3 = {s3}\nS4 = {s4}\nS5 = {s5}\nS6 = {s6}")