#a:
def a(n):
    p = 1
    for i in range(n + 1):
        p = p * (2 * i + 1)
    return p

#b:
def b(n):
    s = 0
    for i in range(1, n + 1):
        s += ((-1) ** (i + 1)) * i
    return s

#c:
def c(n):
    s = 0
    tong = 0
    for i in range(1, n + 1):
        tong += i
        s += tong
    return s

#d:
def d(x, y, n):
    p = x ** y
    for k in range(1, n + 1):
        p += (x + 3 ** (2 * y) + y ** k)
    return p

print("BÀI 4")

# a, b, c:
n = int(input("Nhập n: "))
print("a) P(n) =", a(n))
print("b) S(n) =", b(n))
print("c) S(n) =", c(n))

# d:
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
n = int(input("Nhập n (n > 1): "))

print("d) P(x,y) =", d(x, y, n))