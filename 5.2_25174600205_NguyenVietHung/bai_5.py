def simple_rand(seed):
    a = 1664525
    c = 1013904223
    m = 2**32
    while True:
        seed = (a * seed + c) % m
        yield seed

gen = simple_rand(12345)  

a = [0]*1000  
i = 0

while i < 1000:
    num = next(gen) % 99999 + 1
    if num % 7 != 0:
        a[i] = num
        i += 1

t = tuple(a) 

print("List:", a[:10])

print("Tuple:", t[:10])