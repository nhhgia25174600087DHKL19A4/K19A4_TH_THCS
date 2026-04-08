username = input("Nhập username: ")
password = input("Nhập password: ")

co_chu_thuong = False
co_chu_hoa = False
co_so = False
co_ky_tu_db = False

for c in password:
    if 'a' <= c <= 'z':
        co_chu_thuong = True
    elif 'A' <= c <= 'Z':
        co_chu_hoa = True
    elif '0' <= c <= '9':
        co_so = True
    elif c in ['$', '#', '@']:
        co_ky_tu_db = True

hop_le = (
    co_chu_thuong and
    co_chu_hoa and
    co_so and
    co_ky_tu_db and
    6 <= len(password) <= 12
)
if hop_le:
    print("Mật khẩu hợp lệ")
else:
    print("Mật khẩu không hợp lệ")