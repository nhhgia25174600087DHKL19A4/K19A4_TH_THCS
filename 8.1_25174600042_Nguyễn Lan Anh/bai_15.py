#a
a = []
for i in range(1, 101):
    if i % 2 == 0:
        a.append(i)
print(a)
#b
def my_reduce(lst):
    s = 0
    for x in lst:
        s += x
    return s
n = int(input("Nhập n: "))
a = []
for i in range(n):
    x = int(input("Nhập số: "))
    a.append(x)

chan = list(filter(lambda x: x % 2 == 0, a))

tong = my_reduce(chan)

print("Danh sách:", a)
print("Số chẵn:", chan)
print("Tổng chẵn:", tong)