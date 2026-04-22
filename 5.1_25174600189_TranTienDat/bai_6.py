thang = hoa = thua = 0

for i in range(5):
    nguoi_choi = input("Nhập (bua/keo/la): ")
    may_tinh = input("Nhập máy (bua/keo/la): ")

    if nguoi_choi == may_tinh:
        hoa += 1
    elif (nguoi_choi == "bua" and may_tinh == "keo") or \
         (nguoi_choi == "keo" and may_tinh == "la") or \
         (nguoi_choi == "la" and may_tinh == "bua"):
        thang += 1
    else:
        thua += 1

print("Thắng:", thang, "Hòa:", hoa, "Thua:", thua)