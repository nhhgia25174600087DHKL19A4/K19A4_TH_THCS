while True:
    print("1:+ 2:- 3:* 4:/ 0:Thoát")
    chon = int(input())

    if chon == 0:
        break

    a = int(input())
    b = int(input())

    kq = {
        1: a + b,
        2: a - b,
        3: a * b,
        4: b and a / b
    }

    print(kq.get(chon, "Sai"))