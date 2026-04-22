seed = 123456789 
A = []
while len(A) < 1000:
    seed = (1103515245 * seed + 12345) % (2**31)    
    so_ngau_nhien = (seed % 99999) + 1    
    if so_ngau_nhien % 7 != 0:
        A.append(so_ngau_nhien)
print(f"Đã sinh xong {len(A)} số thủ công.")
print("10 số đầu tiên là:", A[:10])