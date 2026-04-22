while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))
    if 0 < m < n:
        break
    print("Sai, nhập lại!")

lst = []
for i in range(m, n+1):
    lst.append(i)

even = []
for i in lst:
    if i % 2 == 0:
        even.append(i)

print(even)