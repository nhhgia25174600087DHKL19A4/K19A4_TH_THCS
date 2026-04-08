lst = []
for i in range(1000):
    x = (i * 53 + 7) % 99999 + 1
    lst.append(x)

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print("Không dùng sorted:", lst[:10])
lst2 = sorted(lst)
print("Dùng sorted:", lst2[:10])