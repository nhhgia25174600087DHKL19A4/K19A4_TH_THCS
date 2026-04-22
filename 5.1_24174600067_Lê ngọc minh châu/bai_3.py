while True:
    m = int(input("Nhap m: "))
    n = int(input("Nhap n: "))
    if m > 0 and m < n:
        break
    else:
        print("Nhap lai")
a = []
i = m
while i <= n:
    a = a + [i]
    i = i + 1
b = []
for i in a:
    if i % 2 == 0:
        b = b + [i]
print(b)