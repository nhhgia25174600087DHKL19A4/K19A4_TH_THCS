#a
def P1(n):
    tich = 1
    for i in range(n + 1):
        tich = tich * (2*i + 1)
    return tich
print(P1(3))
#b
def S1(n):
    s = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            s = s - i
        else:
            s = s + i
    return s
print(S1(2))
#c
def S2(n):
    s = 0
    tong_phu = 0
    for i in range(1, n+1):
        tong_phu = tong_phu + i
        s = s + tong_phu
    return s
print(S2(4))
#d
def P2(x, y, n):
    s = 0
    for k in range(1, n+1):
        s = s + (x + 32*y + y**k)
    return x**y + s
print(P2(2,3,4))