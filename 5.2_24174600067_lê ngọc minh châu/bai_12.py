p = input("Nhap password: ")
hop_le = True
if len(p) < 6 or len(p) > 12:
    hop_le = False
co_thuong = False
co_hoa = False
co_so = False
co_db = False
for i in range(len(p)):
    if 'a' <= p[i] <= 'z':
        co_thuong = True
    if 'A' <= p[i] <= 'Z':
        co_hoa = True
    if '0' <= p[i] <= '9':
        co_so = True
    if p[i] == '@' or p[i] == '#' or p[i] == '$':
        co_db = True
if co_thuong and co_hoa and co_so and co_db and hop_le:
    print("Hop le")
else:
    print("Khong hop le")