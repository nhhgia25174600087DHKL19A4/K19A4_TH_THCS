thang = 0
thua = 0
hoa = 0

for i in range(5):
    print("Lượt", i + 1)
    
    nguoi = input("Nhập (bua/keo/la): ")

    if i % 3 == 0:
        may = "bua"
    elif i % 3 == 1:
        may = "keo"
    else:
        may = "la"
    print("Máy chọn:", may)
    if nguoi == may:
        print("Hòa")
        hoa += 1
    elif (nguoi == "bua" and may == "keo") or \
         (nguoi == "keo" and may == "la") or \
         (nguoi == "la" and may == "bua"):
        print("Bạn thắng")
        thang += 1
    else:
        print("Bạn thua")
        thua += 1

    print("-------------------")

print("Kết quả sau 5 lượt:")
print("Thắng:", thang)
print("Hòa:", hoa)
print("Thua:", thua)