import random
A = []
while len(A) < 1000:
    num = random.randint(1, 99999)
    if num % 7 != 0:
        A = A + [num]
print("Đã sinh xong 1000 số.")