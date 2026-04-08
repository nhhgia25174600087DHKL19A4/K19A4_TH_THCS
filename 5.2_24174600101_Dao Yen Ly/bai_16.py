s = input("nhap day so: ")

a = s.split()

dem = 0

for i in range(len(a)):
    if int(a[i]) % 2 == 0:
        dem = dem + 1

print(dem)

t = (dem,)
print(t)