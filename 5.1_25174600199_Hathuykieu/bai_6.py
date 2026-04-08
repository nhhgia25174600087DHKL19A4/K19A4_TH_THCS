import random
lua_chon = ["keo", "bua", "la"]
thang = 0
thua = 0
hoa = 0
for i in range(5):
    nguoi = input("Nhập (keo/bua/la): ").lower()
    may = random.choice(lua_chon)
    print("Máy chọn:", may)
    if nguoi == may:
        hoa += 1
    elif (nguoi == "keo" and may == "la") or \
         (nguoi == "bua" and may == "keo") or \
         (nguoi == "la" and may == "bua"):
        thang += 1
    else:
        thua += 1
print("Số lần thắng:", thang)
print("Số lần hòa:", hoa)
print("Số lần thua:", thua)