def simple_rand(seed):
    a = 1664525
    c = 1013904223
    m = 2**32
    while True:
        seed = (a * seed + c) % m
        yield seed
gen = simple_rand(12345) 
n = 1000
a = [0]*n

for i in range(n):
    a[i] = next(gen) % 99999 + 1
t = tuple(a)
for i in range(n-1):
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print("10 số đầu tăng dần (list):", a[:10])

for i in range(n-1):
    for j in range(n-1-i):
        if a[j] < a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print("10 số đầu giảm dần (list):", a[:10])

print("10 số đầu (tuple gốc):", t[:10])