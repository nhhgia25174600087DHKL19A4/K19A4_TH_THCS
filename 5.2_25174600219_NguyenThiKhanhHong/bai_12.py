n = input("Nhập mật khẩu: ")

# a.
a = any('a' <= c <= 'z' for c in n)

# b.
b = any('0' <= c <= '9' for c in n)

# c. 
c = any('A' <= c <= 'Z' for c in n)

# d. 
d = any(c in "$#@ " for c in n)

# e-f. 
ef = 6 <= len(n) <= 12

if a and b and c and d and ef:
    print("Mật khẩu hợp lệ")
else:
    print("Mật khẩu không hợp lệ")