chon = ["Búa", "Kéo", "Lá"]
thang = 0
hoa = 0
thua = 0

print("Trò chơi Búa - Kéo - Lá (5 lượt). Nhập 0: Búa, 1: Kéo, 2: Lá")

for i in range(5):
    chon_ngau_nhien = id(object()) % 3 
    
    tu_chon = int(input(f"Lượt {i+1} - Lựa chọn của bạn (0/1/2): "))
    
    print(f"Máy ra: {chon[chon_ngau_nhien]}")
    
    if tu_chon == chon_ngau_nhien:
        print("-> Hòa!")
        hoa += 1
    elif (tu_chon == 0 and chon_ngau_nhien == 1) or \
         (tu_chon == 1 and chon_ngau_nhien == 2) or \
         (tu_chon == 2 and chon_ngau_nhien == 0):
        print("-> Bạn thắng!")
        thang += 1
    else:
        print("-> Bạn thua!")
        thua += 1

print("\n--- KẾT QUẢ SAU 5 LƯỢT ---")
print(f"Thắng: {thang} | Hòa: {hoa} | Thua: {thua}")