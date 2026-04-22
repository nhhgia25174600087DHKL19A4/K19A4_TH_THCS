lua_chon = ["Búa", "Kéo", "Lá"]
thang = 0
hoa = 0
thua = 0
for i in range(1, 6):
    print(f"\nLượt chơi thứ {i}:")
    nguoi_chon = input("Mời em chọn (Búa, Kéo, Lá): ").capitalize()
    
    if nguoi_chon not in lua_chon:
        print("Nhập sai rồi, máy thắng lượt này ")
        thua += 1
        continue
    id_ngau_nhien = id(nguoi_chon) 
    index_may = id_ngau_nhien % 3
    may_chon = lua_chon[index_may]    
    print(f"Máy tính chọn: {may_chon}")
    if nguoi_chon == may_chon:
        print("=> Hòa rồi!")
        hoa += 1
    elif (nguoi_chon == "Búa" and may_chon == "Kéo") or \
         (nguoi_chon == "Kéo" and may_chon == "Lá") or \
         (nguoi_chon == "Lá" and may_chon == "Búa"):
        print("=> Em thắng! Giỏi quá!")
        thang += 1
    else:
        print("=> Máy thắng ")
        thua += 1
print("\n--- KẾT QUẢ CUỐI CÙNG ---")
print(f"Thắng: {thang} | Hòa: {hoa} | Thua: {thua}")