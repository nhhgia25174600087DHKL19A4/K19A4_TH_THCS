a = []
for i in range(0,201):
    if i % 5 == 0 and i % 7 == 0:
        a.append(i)
print("Các số chia hết cho 5 và 7:")
print(a)