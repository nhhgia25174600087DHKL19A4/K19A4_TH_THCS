m = int(input("Nhập số nguyên m: "))
n = int(input("Nhập số nguyên n: "))
m_dau, n_dau = m,n
if m < n:
    m,n = n,m
while m != n:
    r = m - n
    m = r
if m < n:
    tam = m
    m = n
    n = tam
print(f"UCLN của{m_dau} và {n_dau} là: {m}")