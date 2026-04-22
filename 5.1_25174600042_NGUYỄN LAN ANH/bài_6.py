import random
thang = 0
thua = 0
hoa = 0

lua_chon = ["kéo","búa","lá"]

for i in range(5):
    print("Lượt", i + 1)

    nguoi = input("Nhập (kéo/búa/lá): ")
    may = random.choice(lua_chon)

    print("May chon: ", may)

    if nguoi == may:
        print("Hòa")
        hoa = hoa + 1
    elif (nguoi == "keo" and may == "la") or \
         (nguoi == "bua" and may == "keo") or \
         (nguoi == "la" and may == "bua"):
        print("Thang")
        thang += 1
    else:
        print("Thua")
        thua += 1

print("Ket qua:")
print("Thang:", thang)
print("Hoa:", hoa)
print("Thua:", thua)