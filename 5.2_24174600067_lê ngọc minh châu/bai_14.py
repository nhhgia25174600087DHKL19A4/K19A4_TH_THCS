n = int(input("Nhap so tuple: "))
a = []
for i in range(n):
    name = input("Ten: ")
    age = int(input("Tuoi: "))
    score = int(input("Diem: "))
    a = a + [(name, age, score)]
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)