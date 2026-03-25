n = int(input("Nhập số: "))
dao = 0
while n > 0:
    digit = n % 10 
    dao = dao * 10 + digit
    n = n // 10
print("Số đảo là:", dao)    