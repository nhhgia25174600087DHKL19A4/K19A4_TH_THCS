a = []
print("Nhap danh sach so:")
check = True
while check:
    n = int(input("Nhap mot so: "))
    if n == 0:
        check = False
    else:
        a.append(n)
print("List ban dau la:", a)
#Cau a
x = int(input("\nNhap x can tim: "))
found = False
for i in range(len(a)):
    if a[i] == x:
        print("Tim thay", x, "tai:", i)
        found = True
if found == False:
    print("Khong tim thay x")
#Cau b
for i in range(len(a)):
    if a[i] == x:
        moi = int(input("Nhap gia tri moi de thay cho x: "))
        a[i] = moi
        break
print("List sau khi sua la:", a)
#Cau c
y = int(input("\nNhap so y muon them: "))
a.insert(0, y)
a.append(y)
vitri_giua = len(a) // 2
a.insert(vitri_giua, y)
print("List sau khi them y vao 3 cho:", a)
#Cau d
print("\nTruoc khi sap xep:", a)
for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] < a[j+1]:
            tam = a[j]
            a[j] = a[j+1]
            a[j+1] = tam
print("Sau khi sap xep giam dan:", a)
#Cau e
vt_xoa = int(input("\nBan muon xoa o vi tri index may? "))
if vt_xoa >= 0 and vt_xoa < len(a):
    print("Truoc khi xoa:", a)
    a.pop(vt_xoa)
    print("Sau khi xoa:", a)
else:
    print("Vi tri nay khong co trong list nhe!")