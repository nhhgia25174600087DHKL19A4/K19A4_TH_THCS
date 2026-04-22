def hinh_tron(r):
    cv = 2 * 3.14 * r
    dt = 3.14 * r * r
    return cv, dt
r = float(input("Nhap ban kinh: "))
cv, dt = hinh_tron(r)
print("Chu vi:", cv)
print("Dien tich:", dt)