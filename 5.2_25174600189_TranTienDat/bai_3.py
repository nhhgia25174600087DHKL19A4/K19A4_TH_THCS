a = []
while True:
    x = int(input())
    if x == 0:
        break
    a.append(x)

# a
duong = []
khac = []
for i in a:
    if i > 0:
        duong.append(i)
    else:
        khac.append(i)

a = duong + khac
print(a)

# b
m = int(input("Nhập m: "))
a.insert(0, m)
a.append(m)
if len(a) >= 5:
    a.insert(4, m)
print(a)