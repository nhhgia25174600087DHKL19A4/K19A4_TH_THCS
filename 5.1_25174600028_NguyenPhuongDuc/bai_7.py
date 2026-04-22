s = input("Nhập chuỗi cần chuẩn hóa: ")
res = ""
is_space = True 
for char in s:
    if char == ' ':
        if not is_space:
            res += ' '
            is_space = True
    else:
        res += char
        is_space = False
if res != "" and res[-1] == ' ':
    temp = ""
    count = 0
    for char in res:
        if count < len(res) - 1:
            temp += char
        count += 1
    res = temp
print(f"Chuỗi chuẩn hóa: '{res}'")