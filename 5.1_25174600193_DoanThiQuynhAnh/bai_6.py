import random

thang = 0
thua = 0
hoa = 0

for i in range(5):
    may = random.randint(1,3)
    nguoi = int(input("1-Bua 2-Keo 3-La: "))

    if nguoi == may:
        hoa += 1
    elif (nguoi == 1 and may == 2) or \
         (nguoi == 2 and may == 3) or \
         (nguoi == 3 and may == 1):
        thang += 1
    else:
        thua += 1

print("Thang:", thang)
print("Hoa:", hoa)
print("Thua:", thua)