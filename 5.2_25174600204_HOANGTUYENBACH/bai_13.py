
s = input("Nhập các mật khẩu: ")

ds = []
temp = ""

for ch in s:
    if ch == ',':
        ds.append(temp)
        temp = ""
    else:
        temp = temp + ch
ds.append(temp)

kq = []

for p in ds:
    while len(p) > 0 and p[0] == ' ':
        p = p[1:]
    while len(p) > 0 and p[-1] == ' ':
        p = p[:-1]

    co_thuong = False
    co_hoa = False
    co_so = False
    co_db = False

    for ch in p:
        if 'a' <= ch <= 'z':
            co_thuong = True
        elif 'A' <= ch <= 'Z':
            co_hoa = True
        elif '0' <= ch <= '9':
            co_so = True
        elif ch == 'S' or ch == '#' or ch == '@':
            co_db = True

    if (co_thuong and co_hoa and co_so and co_db
        and 6 <= len(p) <= 12):
        kq.append(p)

for i in range(len(kq)):
    print(kq[i], end="")
    if i != len(kq) - 1:
        print(",", end="")