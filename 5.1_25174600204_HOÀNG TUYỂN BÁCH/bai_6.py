options = ["bua", "keo", "la"]

win = 0
draw = 0
lose = 0

print("Trò chơi Búa-Kéo-Lá 5 lượt")

# 5 lượt
for i in range(5):
    while True:
        nguoi_choi = input(f"Lượt {i+1}, chọn búa/keo/la: ").lower()
        if nguoi_choi in options:
            break
        else:
            print("Lựa chọn không hợp lệ, nhập lại.")
    may_tinh = options[i % 3]
    print("Máy tính chọn:", may_tinh)
    if nguoi_choi == may_tinh:
        print("Hòa!")
        draw += 1
    elif (nguoi_choi == "bua" and may_tinh == "keo") or \
         (nguoi_choi == "keo" and may_tinh == "la") or \
         (nguoi_choi == "la" and may_tinh == "bua"):
        print("Bạn thắng!")
        win += 1
    else:
        print("Bạn thua!")
        lose += 1
print("\nKết quả sau 5 lượt:")
print("Thắng:", win)
print("Hòa:", draw)
print("Thua:", lose)