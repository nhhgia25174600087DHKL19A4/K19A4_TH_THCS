def tinh_P_a(n):
    if n < 0:
        return 0 
    p = 1
    for i in range(n + 1):
        p *= (2 * i + 1)
    return p

def tinh_S_b(n):
    if n <= 0:
        return 0
    s = 0
    for i in range(1, n + 1):
        if i % 2 != 0: 
            s += i
        else:          
            s -= i
    return s

def tinh_S_c(n):
    if n <= 0:
        return 0
    tong_chinh = 0
    tong_tam = 0
    for i in range(1, n + 1):
        tong_tam += i        
        tong_chinh += tong_tam 
    return tong_chinh

def tinh_P_d(x, y, n):
    # Tính phần x^y
    ket_qua = x ** y
    tong_sigma = 0
    for k in range(1, n + 1):
        tong_sigma += (x + 32 * y + (y ** k))
        
    return ket_qua + tong_sigma