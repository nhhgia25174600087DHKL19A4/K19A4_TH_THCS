so = 123456789 
A = []
while len(A) < 1000:
    so = (1103515245 * so + 12345) % (2**31)
    so_ngau_nhien = (so % 99999) + 1
    if so_ngau_nhien % 7 != 0:
        A.append(so_ngau_nhien)
print(A[:10])