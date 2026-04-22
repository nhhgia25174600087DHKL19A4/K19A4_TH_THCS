import random
ds = []
for i in range(201):
    if i % 5 == 0 and i % 7 == 0:
        ds += [i]
print("Danh sách:", ds)
x = random.choice(ds)
print("Số ngẫu nhiên:", x)