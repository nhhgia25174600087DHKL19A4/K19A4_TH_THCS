a = [0] * 1000

for i in range(1000):
    a[i] = i + 1   

# cach 1: sap xep tang 

b = [0] * 1000
for i in range(1000):
    b[i] = a[i]

for i in range(1000):
    for j in range(i+1, 1000):
        if b[i] > b[j]:
            temp = b[i]
            b[i] = b[j]
            b[j] = temp

print("tang dan:")
for i in range(20):  
    print(b[i], end=" ")
print()

# cach 2: sap xep giam

for i in range(1000):
    for j in range(i+1, 1000):
        if a[i] < a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print("giam dan:")
for i in range(20):  
    print(a[i], end=" ")