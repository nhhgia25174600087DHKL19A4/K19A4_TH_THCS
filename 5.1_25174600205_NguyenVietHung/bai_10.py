n = int(input("Nhập n: "))

lst = [0] * n
for i in range(n):
    lst[i] = i + 1
odd = [0] * n
count = 0

for i in range(n):
    if lst[i] % 2 != 0:
        odd[count] = lst[i]
        count += 1

tp = tuple(odd[:count])

print("Tuple số lẻ:", tp)