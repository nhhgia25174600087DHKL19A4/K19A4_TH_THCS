may = ["bua", "keo", "la"]
thang = 0
hoa = 0
thua = 0
for i in range(5):
    nguoi = input("Nhap (bua/keo/la): ")
    m = may[i % 3]
    print("May ra:", m)
    if nguoi == m:
        hoa += 1
    elif (nguoi == "bua" and m == "keo") or \
         (nguoi == "keo" and m == "la") or \
         (nguoi == "la" and m == "bua"):
        thang += 1
    else:
        thua += 1
print("Thang:", thang)
print("Hoa:", hoa)
print("Thua:", thua)