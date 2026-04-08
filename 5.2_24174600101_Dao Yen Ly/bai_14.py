a = list(map(int, input("nhap list: ").split()))

# a. dao nguoc list
b = [0] * len(a)
k = 0

for i in range(len(a)-1, -1, -1):
    b[k] = a[i]
    k = k + 1

print("dao nguoc:")
for i in range(len(b)):
    print(b[i], end=" ")
print()

# b. sap xep tang dan 

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print("sap xep tang:")
for i in range(len(a)):
    print(a[i], end=" ")