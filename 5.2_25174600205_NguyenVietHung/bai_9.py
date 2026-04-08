n = int(input("Nhập n: "))
a = [0]*n
for i in range(n):
    a[i] = int(input("Nhập phần tử thứ " + str(i) + ": "))

max_val = a[0]
min_val = a[0]
for i in range(1,n):
    if a[i] > max_val:
        max_val = a[i]
    if a[i] < min_val:
        min_val = a[i]

print("Max:", max_val)
print("Min:", min_val)

t = tuple(a)
print("Tuple:", t)