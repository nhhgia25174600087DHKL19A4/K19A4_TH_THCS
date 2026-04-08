s = input("Nhập chuỗi: ")
ket_qua = ""
dang_space = False
for c in s.strip():
    if c == " ":
        if not dang_space:
            ket_qua += " "
        dang_space = True
    else:
        ket_qua += c
        dang_space = False
print(ket_qua)