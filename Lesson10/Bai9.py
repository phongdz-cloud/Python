# /*
#     Viết chương trình đổi chữ cái đầu tiên của mỗi từ trong một chuỗi thành chứ hoa
# */
def solution(s):
    if 'a' <= s[0] <= 'z':
        s = chr((ord(s[0]) - 32)) + s[1:len(s)]
    for i in range(1, len(s)):
        if 'a' <= s[i] <= 'z' and s[i - 1] == ' ':
            s = s[0:i] + chr((ord(s[i]) - 32)) + s[i + 1:len(s)]
    return s


s = input()
print(solution(s))
