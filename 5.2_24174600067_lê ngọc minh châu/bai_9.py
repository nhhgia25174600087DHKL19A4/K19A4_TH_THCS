a = list(map(int, input("Nhap list: ").split()))
tat_ca_chan = True
for i in range(len(a)):
    if a[i] % 2 != 0:
        tat_ca_chan = False
if tat_ca_chan == True:
    print("Tat ca deu chan")
else:
    print("Co so le")