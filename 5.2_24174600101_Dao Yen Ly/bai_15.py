a = list(map(int, input("nhap list: ").split()))


minn = a[0]

for i in range(len(a)):
    if a[i] < minn:
        minn = a[i]

print(minn)