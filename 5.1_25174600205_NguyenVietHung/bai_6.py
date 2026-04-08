win_rule = ((1, 2), (2, 3), (3, 1))
thang = 0
hoa = 0
thua = 0

for i in range(5):
    print("\nLượt", i + 1)
    print("1. Búa  2. Kéo  3. Lá")

    player = int(input("Bạn chọn: "))
    computer = (i % 3) + 1

    print("Máy chọn:", computer)

    if player == computer:
        hoa += 1
    else:
        is_win = False
        for j in range(3):
            if win_rule[j][0] == player and win_rule[j][1] == computer:
                is_win = True
                break

        if is_win:
            thang += 1
        else:
            thua += 1

print("\nKết quả:")
print("Thắng:", thang)
print("Hòa:", hoa)
print("Thua:", thua)