import random
lst = [i for i in range(201) if i % 5 == 0 and i % 7 == 0]

x = random.choice(lst)

print("Số ngẫu nhiên:", x)