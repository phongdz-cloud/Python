# /*
#     Viết chương trình tính tổng các ký tự số có trong chuỗi
# */
def solution(s):
    flag = False
    temp = sum = 0
    for i in range(0, len(s)):
        if '0' <= s[i] <= '9':
            temp = temp * 10 + int(s[i])
            if i - 1 >= 0 and s[i - 1] == '-':
                flag = True
        else:
            if temp != 0:
                if flag:
                    sum += -1 * temp
                else:
                    sum += temp
                flag = False
                temp = 0
    if flag:
        sum += temp * -1
    else:
        sum += temp
    return sum


s = input()
print(solution(s))
