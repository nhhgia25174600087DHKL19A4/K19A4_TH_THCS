n = int(input("Nhập n: "))
lst = [0] * n
for i in range(n):
    lst[i] = i + 1
prime = [0] * n
p_count = 0
for i in range(n):
    x = lst[i]
    dem = 0

    for j in range(1, x + 1):
        if x % j == 0:
            dem += 1

    if dem == 2:
        prime[p_count] = x
        p_count += 1

perfect = [0] * n
h_count = 0

for i in range(n):
    x = lst[i]
    tong = 0

    for j in range(1, x):
        if x % j == 0:
            tong += j

    if tong == x:
        perfect[h_count] = x
        h_count += 1

print("Số nguyên tố:")
for i in range(p_count):
    print(prime[i], end=" ")

print("\nSố hoàn hảo:")
for i in range(h_count):
    print(perfect[i], end=" ")