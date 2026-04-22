x = int(input("Nhập tử số: "))
while True:
    y = int(input("Nhập mẫu số: "))
    if y != 0:
        break
    print("Mẫu số không được bằng 0. Hãy nhập lại!")

print(f"Phân số: {x}/{y}")