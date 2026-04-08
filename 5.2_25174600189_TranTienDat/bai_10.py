import random

a = [x for x in range(201) if x % 5 == 0 and x % 7 == 0]

print(random.choice(a))