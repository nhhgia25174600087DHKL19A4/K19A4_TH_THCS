tu = int(input("Nhập tử số: "))

while True:
    mau = int(input("Nhập mẫu số (khác 0): "))
    if mau != 0:
        break
    print("Mẫu số phải khác 0, nhập lại!")

# In phân số
print("Phân số là:", tu, "/", mau)