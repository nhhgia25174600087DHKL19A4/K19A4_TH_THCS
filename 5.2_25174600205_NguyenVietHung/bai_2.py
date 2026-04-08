n = int(input())
a = [int(input()) for _ in range(n)]

# a
m1 = max(a)
m2 = None
for x in a:
    if x != m1 and (m2 is None or x > m2):
        m2 = x

print("Max2:", m2)
print("Vị trí:", [i for i,x in enumerate(a) if x == m2] if m2!=None else [])

# b
d = m = 0
for x in a:
    d = d+1 if x>0 else 0
    m = max(m,d)
print("Dài nhất:", m)

# c
s = ms = 0
for x in a:
    s = s+x if x>0 else 0
    ms = max(ms,s)
print("Tổng max:", ms)

print("Tuple:", tuple(a))