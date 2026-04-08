lua_chon = ["bua", "keo", "la"]
thang = 0
hoa = 0
thua = 0
for i in range(5):
    may = lua_chon[i % 3] 
    nguoi = input("Nhập búa/kéo/lá: ")

    print("Máy chọn:", may)

    if nguoi == may:
        hoa += 1
    elif (nguoi == "bua" and may == "keo") or \
         (nguoi == "keo" and may == "la") or \
         (nguoi == "la" and may == "bua"):
        thang += 1
    else:
        thua += 1
print("Kết quả sau 5 lượt:")
print("Thắng:", thang)
print("Hòa:", hoa)
print("Thua:", thua)