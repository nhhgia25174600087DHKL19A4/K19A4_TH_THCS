import random
a=0
b=0
c=0
for i in range(5):
    print("Lượt",i+1)
    nguoi=input("Chọn(bua/keo/la):")
    may=random.choice(["bua","keo","la"])
    print ("Máy chọn:",may)
    if nguoi == may:
        c += 1
    elif (nguoi == "bua" and may == "keo") or \
         (nguoi == "keo" and may == "la") or \
         (nguoi == "la" and may == "bua"):
        a += 1
    else:
        b += 1
print("Thắng:", a)
print("Thua:", b)
print("Hòa:", c)