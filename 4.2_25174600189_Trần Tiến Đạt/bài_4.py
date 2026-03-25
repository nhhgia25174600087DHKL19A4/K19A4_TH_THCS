n = input("Nhập số: ")
i = 0
while i < len(n):
    for j in range(1):
        if n[i] == '0':
            print("không", end=" ")
        elif n[i] == '1':
            print("một", end=" ")
        elif n[i] == '2':
            print("hai", end=" ")
        elif n[i] == '3':
            print("ba", end=" ")
        elif n[i] == '4':
            print("bốn", end=" ")
        elif n[i] == '5':
            print("năm", end=" ")
        elif n[i] == '6':
            print("sáu", end=" ")
        elif n[i] == '7':
            print("bảy", end=" ")
        elif n[i] == '8':
            print("tám", end=" ")
        elif n[i] == '9':
            print("chín", end=" ")
    i += 1