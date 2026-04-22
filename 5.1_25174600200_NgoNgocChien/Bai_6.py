thang = 0
thua = 0 
hoa = 0
for i in range(5):
    print("1: kéo, 2: búa, 3: bao")
    nguoi = int(input("Bạn chọn: "))
    may = int(input("Máy chọn: "))
    if nguoi == may:
        hoa += 1
    elif (nguoi == 1 and may == 3) or \
         (nguoi == 2 and may == 1) or \
         (nguoi == 3 and may == 2):
        thang += 1
    else:
        thua += 1
print("Thắng:", thang)
print("Thua:", thua)
print("Hòa:", hoa)            