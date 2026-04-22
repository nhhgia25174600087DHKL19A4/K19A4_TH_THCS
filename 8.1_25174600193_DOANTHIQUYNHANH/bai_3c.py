def is_palindrome(num):
    return str(num) == str(num)[::-1]

def in_so_doi_xung():
    dem = 0
    for i in range(1001):
        if is_palindrome(i):
            print(f"{i:5}", end="")
            dem += 1
            if dem % 15 == 0:
                print()
    print()

in_so_doi_xung()