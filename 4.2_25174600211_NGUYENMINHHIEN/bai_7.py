print("--- MENU ĐỒ UỐNG ---")
print("1. Cafe\n2. Cam vắt\n3. Nước ép cà rốt\n4. Nước lọc\n5. Nước dừa")

chon = input("Mời bạn chọn món (1-5): ")
menu = {
    "1": "Cafe",
    "2": "Cam vắt",
    "3": "Nước ép cà rốt",
    "4": "Nước lọc",
    "5": "Nước dừa"
}

if chon in menu:
    print(f"Bạn đã chọn: {menu[chon]}")
else:
    print("Lựa chọn không hợp lệ.")