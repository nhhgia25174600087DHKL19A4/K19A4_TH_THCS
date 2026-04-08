s = input("Nhập chuỗi: ")
words = []
word = ""
for c in s:
    if c != " ":
        word += c
    else:
        if word != "":
            words.append(word)
            word = ""
if word != "":
    words.append(word)
result = ""
for i in range(len(words)):
    result += words[i]
    if i != len(words) - 1:
        result += " "
print("Chuỗi chuẩn hóa:", result)