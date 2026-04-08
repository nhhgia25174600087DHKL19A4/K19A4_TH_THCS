ds = []
print("Nhap cac so (nhap 0 de dung lai):")
while True:
    so = int(input("- "))
    if so == 0:
        break
    ds.append(so)
#a
x = int(input("Nhap x can tim: "))
tim_thay = False
for i in range(len(ds)):
    if ds[i] == x:
        print("Tim thay x o vi tri thu:", i)
        tim_thay = True
if tim_thay == False:
    print("Khong co x trong danh sach")
# b
for i in range(len(ds)):
    if ds[i] == x:
        moi = int(input("Nhap gia tri moi de thay cho x: "))
        ds[i] = moi
        break 
print("Danh sach sau khi sua:", ds)
# c
y = int(input("Nhap y muon them: "))
ds.insert(0, y) 
ds.append(y)    
vi_tri_giua = len(ds) // 2
ds.insert(vi_tri_giua, y) 
print("Danh sach sau khi them y:", ds)
#d
print("Truoc khi sap xep:", ds)
for i in range(len(ds)):
    for j in range(i + 1, len(ds)):
        if ds[i] < ds[j]:
            # Doi cho 2 so
            tam = ds[i]
            ds[i] = ds[j]
            ds[j] = tam
print("Sau khi sap xep giam dan:", ds)
# e
print("Danh sach dang co:", ds)
so_xoa = int(input("Ban muon xoa so nao: "))
if so_xoa in ds:
    ds.remove(so_xoa)
    print("Danh sach sau khi xoa:", ds)
else:
    print("So nay khong co de ma xoa")