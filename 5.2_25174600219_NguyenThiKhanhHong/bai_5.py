import random
A = []
while len(A) < 1000:
    so_ngau_nhien = random.randint(1, 99999)
    if so_ngau_nhien % 7 != 0:
        A.append(so_ngau_nhien)
print(f"Đã sinh xong {len(A)} số. 5 số đầu tiên: {A[:5]}")