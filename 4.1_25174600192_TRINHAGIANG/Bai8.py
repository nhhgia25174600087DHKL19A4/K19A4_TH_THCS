def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n): 
        if n % i == 0:
            return False
    return True

print("Các số nguyên tố từ 1 đến 1000 là:")
for num in range(1, 1001):
    if is_prime(num):
        print(num, end=" ")
