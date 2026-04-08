may_tinh_chon = ["bua", "keo", "la", "keo", "bua"] 
thang = 0
hoa = 0
thua = 0

for i in range(5):
    nguoi_choi = input(f"Lượt {i+1} (bua, keo, la): ").lower()
    may = may_tinh_chon[i]
    print(f"Máy chọn: {may}")
    
    if nguoi_choi == may:
        print("Hòa!")
        hoa += 1
    elif (nguoi_choi == "bua" and may == "keo") or \
         (nguoi_choi == "keo" and may == "la") or \
         (nguoi_choi == "la" and may == "bua"):
        print("Bạn thắng!")
        thang += 1
    else:
        print("Bạn thua!")
        thua += 1

print(f"Thống kê: Thắng {thang}, Hòa {hoa}, Thua {thua}")