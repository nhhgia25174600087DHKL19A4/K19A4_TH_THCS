import random

thang = 0
thua = 0
hoa = 0

ds = ["keo", "bua", "la"]

for i in range(5):
    print("Lan", i+1)
    user = input("Chon: ")
    
    may = ds[random.randint(0,2)]
    print("May:", may)
    
    if user == may:
        hoa += 1
        print("Hoa")
    else:
        if user == "keo":
            if may == "la":
                thang += 1
                print("Thang")
            else:
                thua += 1
                print("Thua")
        elif user == "bua":
            if may == "keo":
                thang += 1
                print("Thang")
            else:
                thua += 1
                print("Thua")
        elif user == "la":
            if may == "bua":
                thang += 1
                print("Thang")
            else:
                thua += 1
                print("Thua")

print("Tong ket:")
print("Thang:", thang)
print("Thua:", thua)
print("Hoa:", hoa)