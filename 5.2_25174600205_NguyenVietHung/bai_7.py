a = [["mon", 73], ["tue", 89], ["wed", 95], ["thu", 68], ["fri", 100]]

n = len(a)
tong = 0
for i in range(n):
    tong += a[i][1]

trungbinh = tong / n
print("Diem trung binh:", trungbinh)

max_val = a[0][1]
day = a[0][0]

for i in range(1, n):
    if a[i][1] > max_val:
        max_val = a[i][1]
        day = a[i][0]

print("Ngay diem cao nhat:", day, "Diem:", max_val)

t = tuple(tuple(a[i]) for i in range(n))
print("Tuple:", t)