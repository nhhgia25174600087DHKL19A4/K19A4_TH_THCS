n = input("Nhập vào một số: ")
chu_so = {
    '0': 'không', '1': 'một', '2': 'hai', '3': 'ba', '4': 'bốn',
    '5': 'năm', '6': 'sáu', '7': 'bảy', '8': 'tám', '9': 'chín'
}
# --- CÁCH 1: DÙNG VÒNG LẶP FOR ---
print("Kết quả (Dùng FOR):", end=" ")
for ky_tu in n:
    if ky_tu in chu_so:
        print(chu_so[ky_tu], end=" ")
print() 

# --- CÁCH 2: DÙNG VÒNG LẶP WHILE ---
print("Kết quả (Dùng WHILE):", end=" ")
i = 0
while i < len(n):
    ky_tu = n[i]
    if ky_tu in chu_so:
        print(chu_so[ky_tu], end=" ")
    i += 1
print()