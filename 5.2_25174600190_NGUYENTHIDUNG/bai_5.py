lst = []
i = 1
while len(lst) < 1000:
    x = (i * 37 + 13) % 99999 + 1 
    if x % 7 != 0:
        lst.append(x)
    i += 1

print("Độ dài:", len(lst))
print(lst[:10])