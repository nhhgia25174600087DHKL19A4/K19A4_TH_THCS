n =int(input("Nhập n: "))
m =int(input("Nhập m: "))
ds = []
for i in range(1, n + 1):
    ds.append(i*i)
if m >= n:
    print(ds)
else:
    print(ds[:m])