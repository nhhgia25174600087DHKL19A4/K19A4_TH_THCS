
n = int(input("Nhập số lượng phần tử trong list: "))

ds = [] 

for i in range(n):
    while True:  
        x = int(input(f"Nhập phần tử thứ {i+1} (phải là số chẵn): "))
        if x % 2 == 0:
            ds.append(x)
            break  
        else:
            print("Sai! Phải nhập số chẵn, nhập lại.")

print("\nDanh sách các số chẵn đã nhập:", ds)