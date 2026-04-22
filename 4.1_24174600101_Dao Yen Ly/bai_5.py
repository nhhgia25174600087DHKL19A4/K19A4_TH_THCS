n = int(input("Nhap so nguyen: "))
dao = 0

while n != 0:
    dao = dao * 10 + n % 10
    n //= 10

print("So dao nguoc:", dao)