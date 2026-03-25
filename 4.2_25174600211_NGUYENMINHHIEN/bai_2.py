tu_so = int(input("Nhập tử số: "))
while True:
    mau_so = int(input("Nhập mẫu số: "))
    if mau_so != 0:
        break
    print("Mẫu số phải khác 0. Nhập lại!")
print(f"Phân số vừa nhập: {tu_so}/{mau_so}")