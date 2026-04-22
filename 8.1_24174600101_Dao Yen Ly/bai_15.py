# phan a:
def in_so_chan():
    for i in range(1, 101):
        if i % 2 == 0:
            print(i, end=" ")

in_so_chan()

# phan b:
n = int(input("Nhap so luong: "))
s = 0
dem = 0
while dem < n:
    x = input("Nhap so: ")
    
    if x == "":
        print("Ban chua nhap gi, nhap lai!")
        continue
    a = int(x)
    if a % 2 == 0:
        s = s + a
    dem = dem + 1
print("Tong so chan la:", s)