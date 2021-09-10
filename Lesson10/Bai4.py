# /*
#     Viết chương trình đếm số từ trong một chuỗi đa nhập từ bàn phím
# */
def removeSpace(s):
    while s[0] == " ":
        s = s[1::]
    while s[len(s) - 1] == " ":
        s = s[:-1:]
    i = 0
    while i < len(s) - 1:
        if s[i] == " " and s[i + 1] == " ":
            s = s[0:i:] + s[i + 1::]
        else:
            i += 1
    return s


s = input()
s = removeSpace(s)
print(len(s.split(" ")))
